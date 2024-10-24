from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def api_endpoint():
    arg = request.get_json()
    print(arg)
    arg1 = arg.get('timestamp')
    arg2 = arg.get('local IP')
    
#    if not arg1 or not arg2:
#        return jsonify({'error': 'Missing arguments'}), 400
    
    # Beispiel-Logik: Argumente zusammenfügen
    result = f"{arg1} {arg2}"
    
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)
