from django.conf import settings

import requests


class Paystack():
    PAYSTACK_SECRET_KEY = "sk_test_7515a3e58c6c638eefbc4c375567b051b869d0fc"
    base_url = 'https://api.paystack.co'

    def verify_payment(self, reference, *args, **kwargs):
        #print(self.PAYSTACK_SECRET_KEY)
        path = f"/transaction/verify/{reference}"
       

        headers = {
            "Authorization":f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "Content-Type":"application/json",
        }
        url = self.base_url + path
        response = requests.get(url, headers=headers)
        men = str(self.PAYSTACK_SECRET_KEY)
       
        print(response)

        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data['status'],  response_data['data']
        
        response_data = response.json()
        print(response_data)
        return response_data["status"], response_data["message"], men
