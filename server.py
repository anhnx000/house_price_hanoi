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



@app.route('/dudoan')
def dudoan():
    return jsonify([1200000, 0.3])


# @app.route('/<DienTich>/<SoPhongNgu>/<SoToilet>/<HuongNha>/<HuongBanCong/<NoiThat>/<ChuDauTu>')
@app.route('/timthongtin')
def get():
    dict = request.args.to_dict()

    if 'DienTich' in dict:
        DienTich = dict['DienTich']
    if 'SoPhongNgu' in dict:
        SoPhongNgu = dict['SoPhongNgu']
    if 'SoToilet' in dict:
        SoToilet = dict['SoToilet']
    if 'HuongNha' in dict:
        HuongNha = dict['HuongNha']
    if 'HuongBanCong' in dict:
        HuongBanCong = dict['HuongBanCong']
    if 'NoiThat' in dict:
        NoiThat = dict['NoiThat']
    if 'ChuDauTu' in dict:
        ChuDauTu = dict['ChuDauTu']

    conn = sqlite3.connect('XA.db');
    cur = conn.cursor()
    DienTich = dict['DienTich']
    SoPhongNgu = dict['SoPhongNgu']
    SoToilet = dict['SoToilet']
    HuongNha = dict['HuongNha']
    HuongBanCong = dict['HuongBanCong']
    NoiThat = dict['NoiThat']
    ChuDauTu = dict['ChuDauTu']
    dau  = DienTich*90/100
    cuoi = DienTich*110/100
    query = cur.execute(
        f"select Location from data where NumberBed = {SoPhongNgu} and NumberToilet = {SoToilet} group by Location  having Area > {dau}  ")  # Dòng này thực hiện truy vấn và trả về json

    r = [dict((cur.description[i][0], value) \
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    kq = (r[0] if r else None) if one else r
    ok = dumps(kq)
    #     return jsonify({'employees': [i[0] for i in query.fetchall()]})  # Tìm và thêm cột đầu tiên là Employee ID
    # c = conn.cursor()
    # em =  c.execute('SELECT top')ỉ;
    # import pandas as pd
    # ok = query.fetchall()
    print(t)
    return ok


# @app.route('/<ho>/<ten>', methods=['GET'])
# def test(ho=None, ten=None):
#     # em =  c.execute('SELECT top')ỉ
#     # import pandas as pd
#
#     return json(ok)


if __name__ == '__main__':
    app.run(debug=True)
