import suds
import ysApi

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")


    try:
        print("Cancelling the Signature ... ")

        # For the last signature
        last = c.getListSign(count=1)
        idDemand = last[0]['cosignatureEvent']

        res = c.cancelSignatureDemand(idDemand)
        print(res)

    except ysApi.ApiError as error:
        print(error)