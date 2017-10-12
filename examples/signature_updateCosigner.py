import suds
import ysApi
from ysApi import Signer

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")


    try:
        print("Updating the Signature ... ")

        token = '9hqft6NVLb8LrRdxgkKt0hsraFXd6CLn4qcyrMGH'
        signer = Signer(firstName='Jon', lastName='Snow', phone='+212600000000', mail='knows.nothing@example.com') 

        res = c.updateCosigner(token, signer)
        print(res)

    except ysApi.ApiError as error:
        print(error)