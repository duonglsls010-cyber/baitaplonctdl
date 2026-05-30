from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Danh sách lưu trữ dữ liệu thuốc ban đầu
danh_sach_thuoc = [
    {"maThuoc": "T001", "tenThuoc": "Paracetamol 500mg", "nhaSX": "Dược Hậu Giang", "soLuong": 100, "giaBan": 35000},
    {"maThuoc": "T002", "tenThuoc": "Amoxicillin", "nhaSX": "Imexpharm", "soLuong": 50, "giaBan": 42000}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/thuoc', methods=['GET'])
def get_thuoc():
    return jsonify(danh_sach_thuoc)

@app.route('/api/thuoc', methods=['POST'])
def add_thuoc():
    data = request.json
    thuoc_moi = {
        "maThuoc": data['maThuoc'],
        "tenThuoc": data['tenThuoc'],
        "nhaSX": data['nhaSX'],
        "soLuong": int(data['soLuong']),
        "giaBan": float(data['giaBan'])
    }
    danh_sach_thuoc.append(thuoc_moi)
    return jsonify({"status": "success"})

@app.route('/api/thuoc/search', methods=['GET'])
def search_thuoc():
    tu_khoa = request.args.get('q', '').lower()
    ket_qua = [t for t in danh_sach_thuoc if tu_khoa in t['tenThuoc'].lower()]
    return jsonify(ket_qua)

@app.route('/api/thuoc/sort', methods=['GET'])
def sort_thuoc():
    n = len(danh_sach_thuoc)
    for i in range(n):
        for j in range(0, n-i-1):
            if danh_sach_thuoc[j]['giaBan'] > danh_sach_thuoc[j+1]['giaBan']:
                danh_sach_thuoc[j], danh_sach_thuoc[j+1] = danh_sach_thuoc[j+1], danh_sach_thuoc[j]
    return jsonify(danh_sach_thuoc)

if __name__ == '__main__':
    app.run(debug=True)