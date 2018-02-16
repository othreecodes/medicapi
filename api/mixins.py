import requests
from django.conf import settings
import wolframalpha


class BotMixin(object):
    def fetch_data_from_grits(self, diagnosis):
        data = {"content": diagnosis, "api_key": settings.GRITS_API_KEY}

        response = requests.get(settings.GRITS_BASE_URL, params=data)
        # if response.status_code == 200:
        data = response.json()
        diseases = data.get('diseases')
        disease_name = ""
        prob = 0
        d_index = None
        if diseases:
            for index, disease in enumerate(diseases):

                if disease['probability'] + sum([
                        x.get('score') or 0
                        for x in disease['inferred_keywords']
                ]) + sum([x.get('score') or 0
                          for x in disease['keywords']]) > prob:
                    disease_name = disease['name']
                    prob = disease['probability']
                    d_index = index

            return self.get_wolfman_data(disease_name)
        else:
            return None

    def get_wolfman_data(self, disease):
        client = wolframalpha.Client(settings.WOLFMAN_APP_ID)

        res = client.query(disease)

        return {
            "disease": disease,
            "details": res.details or None,
            "treatment": "Consult a Doctor"
        }

    def get_treatment(self, disease):
        url = 'https://api.fda.gov/drug/label.json?search="{}"&limit=1'.format(
            disease)

        response = requests.get(url)

        if response.status_code == 200:
            
            return response.json().get('results')
        else:
            return None