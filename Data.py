import requests
import json
import psycopg2 as pg

db_host = "localhost"
database = "Alien"
db_user = "postgres"
db_pwd = "Ashes4567v"


class AlienLanguage:
    def __init__(self):
        #self._logger = logger
        self._db_conn = None

        try:
            self._db_conn = pg.connect(host=db_host, database=database, user=db_user, password=db_pwd)
            #self._logger.info('Successfully connected to the Database!')
        except Exception as e:
            #self._logger.info('Connecting to the Database Failed!')
            #self._logger.error(e)
            Exception('Connecting to the Database Failed!')

    def english_to_dorbdorb(self,english):
        url = "https://72exx40653.execute-api.us-east-1.amazonaws.com/prod/translateEnglishToAlien"
        data = {"textToTranslate": english}
        response = requests.post(url, json.dumps(data))
        return response.json()

    def dorbdorb_to_gorbyoyo(self,dorbdorb):
        arr = dorbdorb #duplicate array
        lst2=[]
        for i in range(len(arr)):
            k=0
            dorbdorb = arr[i]
            for char in dorbdorb:
                if char.isdigit(): #count how many digits occur before alpha
                    k = k+1
                else:
                    break
            if k == 2:
                split = [0, 2, 3] #split string depending on how many digits appear before alpha
            elif k == 3:
                split = [0, 3, 4]
            lst = [dorbdorb[i:j] for i, j in zip(split, split[1:] + [None])]
            integer1 = [lst[0]]
            alpha = [lst[1]]
            integer2 = [lst[2]]
            alpha.append("yo")
            for j in range(len(integer1)):
                sum_int = [int(integer1[j]) + int(integer2[j])]
                translation = alpha + sum_int
                s = [str(j) for j in translation]
                res = "".join(s)
                lst2.append(res)
        return lst2

    def verify_translation(self,gorbyoyo):
        url = "https://72exx40653.execute-api.us-east-1.amazonaws.com/prod/confirmtranslation"
        data = {"textToVerify": gorbyoyo}
        response = requests.post(url, json.dumps(data))
        message = response.text
        if message == "Success":
            return gorbyoyo
        elif message == "Invalid translation":
            return "Failed to Translate"

    def contacenate(self,gorbyoyo):
        for j in range(len(gorbyoyo)):
            result = "".join(gorbyoyo)
        try:
            cursor = self._db_conn.cursor()
            values = cursor.mogrify("(%s)", result).decode('utf-8')
            cursor.execute('insert into translations values ' + values)
            self._db_conn.commit()
            self._logger.info('Successfully inserted translation %s into the Database.' % result)
        except Exception as e:
            self._logger.error(e)
            self._db_conn.rollback()
        finally:
            cursor.close()
            return result

