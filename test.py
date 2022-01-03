from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from json import dumps
import sqlite3

app = Flask(__name__)
api = Api(app)



# conn = sqlite3.connect('XA.db')
# cur = conn.cursor()
# DienTich = 90
# dau  = DienTich*90/100
# cuoi = DienTich*110/100
# query = cur.execute(
#     f"select Location from data where NumberBed = 3 and NumberToilet = 2 group by Location  having Area > {dau} ")  # Dòng này thực hiện truy vấn và trả về json
#
# ok = query.fetchall()
# print(ok)

# AA = 90
# conn = sqlite3.connect('XA.db')
# cur = conn.cursor()
# query = cur.execute(
#     "select Location from data where Area = 100.0 and  NumberBed = 3 and NumberToilet = 2 ")  # Dòng này thực hiện truy vấn và trả về json

#
# ok = query.fetchall()
# print(ok)


# @app.route('/<DienTich>/<SoPhongNgu>/<SoToilet>/<HuongNha>/<HuongBanCong>/<NoiThat>/<ChuDauTu>')
@app.route('/timthongtin')
def timthongtin(one = False):
    input = request.args.to_dict()

    if 'DienTich' in input:
        DienTich = input['DienTich']
    if 'SoPhongNgu' in input:
        SoPhongNgu = input['SoPhongNgu']
    if 'SoToilet' in input:
        SoToilet = input['SoToilet']
    if 'HuongNha' in input:
        HuongNha = input['HuongNha']
    if 'HuongBanCong' in input:
        HuongBanCong = input['HuongBanCong']
    if 'NoiThat' in input:
        NoiThat = input['NoiThat']
    if 'ChuDauTu' in input:
        ChuDauTu = input['ChuDauTu']

    conn = sqlite3.connect('XA16.db');
    cur = conn.cursor()

    query = cur.execute(f"select TieuDe from (select  * from data16 as ok) ")
    # # Dòng này thực hiện truy vấn và trả về json
    #
    r = [dict((cur.description[i][0], value) \
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    kq = (r[0] if r else None) if one else r
    ok = dumps(kq)

    # input['SoPhongNgu'
    # SoToilet = input['SoToilet']
    # HuongNha = input['HuongNha']
    # HuongBanCong = input['HuongBanCong']
    # NoiThat = input['NoiThat']
    # ChuDauTu = input['ChuDauTu']
    return jsonify(input)


if __name__ == '__main__':
    app.run(debug=True)
