from flask import Flask, request, jsonify
   from flask_cors import CORS
   import os

   app = Flask(__name__)
   CORS(app)

   @app.route('/calculate', methods=['POST'])
   def calculate():
       data = request.json
       first_operand = data['firstOperand']
       second_operand = data['secondOperand']
       operator = data['operator']
       
       try:
           if operator == '+':
               result = first_operand + second_operand
           elif operator == '-':
               result = first_operand - second_operand
           elif operator == '*':
               result = first_operand * second_operand
           elif operator == '/':
               if second_operand == 0:
                   return jsonify({"error": "除数不能为零"}), 400
               result = first_operand / second_operand
           else:
               return jsonify({"error": "无效的操作符"}), 400
           
           return jsonify({"result": result})
       except Exception as e:
           return jsonify({"error": str(e)}), 500

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
