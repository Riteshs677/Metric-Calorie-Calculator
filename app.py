from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='static')

class MetricCalorieCalculator:
    def calculate_bmr(self, age, gender, height, weight):
        """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation"""
        if gender == "male":
            return (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            return (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    def calculate_macros(self, tdee):
        """Calculate macronutrient distribution (30% protein, 40% carbs, 30% fat)"""
        protein_pct = 0.3
        carbs_pct = 0.4
        fat_pct = 0.3
        
        # Calculate grams (4 cal/g for protein and carbs, 9 cal/g for fat)
        protein_g = int((tdee * protein_pct) / 4)
        carbs_g = int((tdee * carbs_pct) / 4)
        fat_g = int((tdee * fat_pct) / 9)
        
        return {
            "protein": {"percentage": protein_pct * 100, "grams": protein_g},
            "carbs": {"percentage": carbs_pct * 100, "grams": carbs_g},
            "fat": {"percentage": fat_pct * 100, "grams": fat_g}
        }

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    calculator = MetricCalorieCalculator()
    bmr = calculator.calculate_bmr(
        age=data['age'],
        gender=data['gender'],
        height=data['height'],
        weight=data['weight']
    )
    tdee = bmr * data['activity_level']
    
    macros = calculator.calculate_macros(tdee)
    
    return jsonify({
        "bmr": round(bmr),
        "tdee": round(tdee),
        "macros": macros
    })

if __name__ == '__main__':
    app.run(debug=True)