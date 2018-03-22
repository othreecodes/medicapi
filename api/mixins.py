import requests
from django.conf import settings
import wolframalpha
from pyfcm import FCMNotification
import arrow

fcm = FCMNotification(api_key=settings.FCM_API_KEY)


class BotMixin(object):

    def fetch_data_from_grits(self, diagnosis):
        data = {"content": diagnosis, "api_key": settings.GRITS_API_KEY}

        response = requests.get(settings.GRITS_BASE_URL, params=data)
        # if response.status_code == 200:
        data = response.json()
        diseases = data.get('diseases')
        disease_name = ""
        self.disease_names = []
        prob = 0
        d_index = None
        if diseases:
            for index, disease in enumerate(diseases):
                if disease['probability'] + sum(
                    [x.get('score') or 0 for x in disease['inferred_keywords']]
                ) + sum(
                    [x.get('score') or 0 for x in disease['keywords']]
                ) > prob:
                    disease_name = disease['name']
                    self.disease_names.append(disease_name)
                    prob = disease['probability']
                    d_index = index

            return self.get_wolfman_data(disease_name)

        else:
            return None

    def get_wolfman_data(self, disease):
        client = wolframalpha.Client(settings.WOLFMAN_APP_ID)

        # res = client.query(disease)

        return {
            "disease": str(self.disease_names),
            "details": None,
            "treatment": "Consult a Doctor",
        }

    def get_treatment(self, disease):
        url = 'https://api.fda.gov/drug/label.json?search="{}"&limit=1'.format(
            disease
        )

        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get('results')

        else:
            return None

    def send_message_to_topic(self, topic, data):
        # {'alerts': [{'date': '2018-03-02 00:19:00-0500',
        # 'descr': 'Nigeria: Seven Children Died of Meningitis Outbreak, 104 Affected ...',
        # 'disease': 'Meningitis',
        # 'disease_ids': ['84', '100'],
        # 'diseases': ['Meningitis', 'Whooping Cough'],
        # 'feed': 'Google News',
        # 'formatted_date': ' 2 March 2018 00:19:00 EST',
        # 'link': 'http://healthmap.org/ln.php?5662572',
        # 'rating': {'count': 0, 'rating': 4},
        # 'reviewed': '2018-03-05 08:57:47-0500',
        # 'species': ['Humans', 'Humans'],
        # 'species_ids': ['132', '132'],
        # 'summary': 'Nigeria: Seven Children Died of Meningitis Outbreak, 104 Affected ... - AllAfrica.com'}
        sd = [
            new
            for new in data
            if arrow.get(new['date']).day >= (arrow.get().day - 2)
        ]

        # fcm.notify_topic_subscribers(
        #     topic_name="news",
        #     data_message=sd[1],
        # )
        for i in sd:
            fcm.notify_topic_subscribers(
                topic_name="news", data_message=i,
            )
