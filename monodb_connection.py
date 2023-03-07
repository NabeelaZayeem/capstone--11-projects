import pymongo
import threading
from pymongo import MongoClient


cl=MongoClient("mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
db=cl['hcl_data']
col=db['train_data']
lock=threading.Lock()
def read():
        lock.acquire()
        try:
            result=col.find({},{"_id":0})
            for r in result:
                print(r)
        finally:
            # pass
             lock.release()
# #read()

def update_tkt(seats):
        lock.acquire()
        try:
            #access the shared resource
            r=col.find_one({},{"_id":0})
            avail=r["No_of_seats"]
            avail=avail- seats
            up_qury={"$set":{"No_of_seats":avail}}
            fil_cd={"Train_no":12345}
            col.update_one(fil_cd,up_qury)
        finally:
            lock.release()
                #release the lock after accessing the shared resource
                # lock.release()
read()

update_tkt(8)
# read()
# tr=Booktrain()
# tr.read()
# tr.update_tkt()