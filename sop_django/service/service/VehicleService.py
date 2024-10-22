from service.models import Vehicle
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains vehicle business logics
'''


class VehicleService(BaseService):



    def search(self, params):
        pageNo = (params['pageNo'] - 1) * self.pageSize
        sql = "select * from sos_vehicle where 1=1"
        val = params.get("vehicleName", None)
        if DataValidator.isNotNull(val):
            sql += " and vehicleName = '" + val + "' "
        sql += " limit %s,%s"
        cursor = connection.cursor()
        print("----------", sql, pageNo, self.pageSize)
        params['index'] = ((params['pageNo'] - 1) * self.pageSize) + 1
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('id', 'vehicleId', 'vehicleName', 'vehicleType', 'purchaseDate', 'buyerName','tid')
        res = {
            "data": [],
            "MaxId": 1,
        }
        count = 0
        res["index"] = params["index"]
        for x in result:
            params['MaxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        print("MMMMMMMMMM", params.get("MaxId"))
        return res

    def search1(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        print("-------pageNo-->>", pageNo)
        sql = "select * from sos_vehicle where 1!=1"
        val1 = params.get("vehicleId", None)
        val2 = params.get("vehicleType", None)
        val3 = params.get("purchaseDate", None)
        val4 = params.get("buyerName", None)
        val5 = params.get("vehicleName", None)

        print("-----val-->>", val1)
        if DataValidator.isNotNull(val1):
            sql += " or vehicleId like '" + val1 + "%%'"
        if DataValidator.isNotNull(val2):
            sql += " or vehicleType = '" + val2 + "' "
        if DataValidator.isNotNull(val3):
            sql += " or purchaseDate = '" + val3 + "' "

        if DataValidator.isNotNull(val4):
            sql += " or buyerName like  '" + val4 + "%%' "

        if DataValidator.isNotNull(val5):
            sql += " or vehicleName like  '" + val5 + "%%' "

            print("-------sql-->>", sql)
        sql += " limit %s,%s"
        print("-------sql-->>", sql)
        cursor = connection.cursor()
        params["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('id', 'vehicleId', 'vehicleName', 'vehicleType', 'purchaseDate', 'buyerName','tid')
        res = {
            "data": [],
            "MaxId": 1,
        }
        count = 0
        res["index"] = params["index"]
        for x in result:
            # print("--------with column-->>",{columnName[i] :  x[i] for i, _ in enumerate(x)})
            params['MaxId'] = x[0]
            print("-------params['MaxId']-->>", params['MaxId'])
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get_model(self):
        return Vehicle
