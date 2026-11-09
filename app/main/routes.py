from app.content.content_data import ABOUT_ME_PARAGRAPHS, COMMUNITY_CHANNELS
from flask import Blueprint, render_template, jsonify
from app.questions import QUIZ_DATA

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@main_bp.route("/dashboard")
def dashboard():
    return render_template(
        'dashboard.html',
        about_paragraphs=ABOUT_ME_PARAGRAPHS,
        channels=COMMUNITY_CHANNELS,
    )

@main_bp.route("/get-quiz/<category>")
def get_quiz(category):
    questions = QUIZ_DATA.get(category, [])
    return jsonify(questions if questions else {"error": "Soru bulunamadı"})


@main_bp.route("/basic-info")
def temel_bilgiler_dersi():
    return render_template("lessons/temel_bilgiler.html")

@main_bp.route("/lessons/unit-1/code-execution")
def kod_calisma_sirasi_dersi():
    return render_template("lessons/kod_calisma_sirasi.html")

@main_bp.route("/lessons/unit-1/data-types")
def veri_tipleri_dersi():
    return render_template("lessons/data_types.html")

@main_bp.route("/lessons/unit-1/numbers-random")
def sayilar_ve_rastgele_dersi():
    return render_template("lessons/numbers_and_random.html")

@main_bp.route("/lessons/unit-1/strings")
def strings_dersi():
    return render_template("lessons/strings.html")

@main_bp.route("/lessons/unit-1/booleans")
def booleans_dersi():
    return render_template("lessons/booleans.html")

@main_bp.route("/lessons/unit-1/operators")
def operatorler_dersi():
    return render_template("lessons/operators.html")

@main_bp.route("/lessons/unit-1/lists")
def listeler_dersi():
    return render_template("lessons/lists.html")

@main_bp.route("/lessons/unit-1/tuples")
def tuple_dersi():
    return render_template("lessons/tuples.html")

@main_bp.route("/lessons/unit-1/sets")
def setler_dersi():
    return render_template("lessons/sets.html")

@main_bp.route("/lessons/unit-1/dictionaries")
def dictionary_dersi():
    return render_template("lessons/dictionaries.html")

@main_bp.route("/lessons/unit-1/conditions")
def kosullar_dersi():
    return render_template("lessons/conditions.html")

@main_bp.route("/lessons/unit-1/loops-and-match")
def donguler_ve_match_dersi():
    return render_template("lessons/loops_and_match.html")

@main_bp.route("/lessons/unit-1/functions")
def fonksiyonlar_dersi():
    return render_template("lessons/functions.html")

@main_bp.route("/lessons/unit-1/sequences-and-arrays")
def diziler_dersi():
    return render_template("lessons/sequences_and_arrays.html")

@main_bp.route("/lessons/unit-1/iterators_and_modules")
def iterators_and_modules_dersi():
    return render_template("lessons/iterators_and_modules.html")

@main_bp.route("/lessons/unit-1/datetime-math-json")
def datetime_math_json_dersi():
    return render_template("lessons/datetime_math_json.html")

@main_bp.route("/lessons/unit-1/regex")
def regex_dersi():
    return render_template("lessons/regex.html")

@main_bp.route("/lessons/unit-1/pip-and-exceptions")
def pip_exceptions_dersi():
    return render_template("lessons/pip_and_exceptions.html")

@main_bp.route("/lessons/unit-1/string-formatting")
def string_formatlama_dersi():
    return render_template("lessons/string_formatting.html")

@main_bp.route("/lessons/unit-1/none-input-venv")
def none_input_venv_dersi():
    return render_template("lessons/none_input_venv.html")

@main_bp.route("/lessons/unit-2/oop-architecture")
def oop_architecture_dersi():
    return render_template("lessons/oop_architecture.html")

@main_bp.route("/lessons/unit-3/file-handling")
def file_handling_dersi():
    return render_template("lessons/file_handling.html")

@main_bp.route("/lessons/unit-4/modules-concept")
def modules_concept_dersi():
    return render_template("lessons/modules_concept.html")

@main_bp.route("/lessons/unit-4/math_and_random")
def math_and_random_dersi():
    return render_template("lessons/math_and_random.html")

@main_bp.route("/lessons/unit-4/advanced_ecosystem")
def advanced_ecosystem_dersi():
    return render_template("lessons/advanced_ecosystem.html")

@main_bp.route("/lessons/unit-5/matplotlib-visualization")
def matplotlib_visualization_dersi():
    return render_template("lessons/matplotlib_visualization.html")

@main_bp.route("/lessons/unit-5/machine-learning-stats")
def ml_stats_dersi():
    return render_template("lessons/machine_learning_stats.html")

@main_bp.route("/lessons/unit-5/predictive-machine-learning")
def predictive_ml_dersi():
    return render_template("lessons/predictive_machine_learning.html")

@main_bp.route("/lessons/unit-6/linear-data-structures")
def linear_data_structures_dersi():
    return render_template("lessons/linear_data_structures.html")

@main_bp.route("/lessons/unit-6/nonlinear-structures")
def nonlinear_structures_dersi():
    return render_template("lessons/nonlinear_hash_structures.html")

@main_bp.route("/lessons/unit-6/searching-and-basic-sorting")
def searching_and_basic_sorting_dersi():
    return render_template("lessons/searching_and_basic_sorting.html")

@main_bp.route("/lessons/unit-6/advanced-salgorithms")
def advanced_algorithms_dersi():
    return render_template("lessons/advanced_algorithms.html")

@main_bp.route("/lessons/mongodb-crud")
def mongodb_crud():
    return render_template("lessons/mongodb_crud.html")

@main_bp.route("/lessons/unit-7/mysql-operations")
def mysql_operations():
    return render_template("lessons/mysql_operations.html")

@main_bp.route("/lessons/unit-8/string_and_list_methods")
def string_and_list_methods():
    return render_template("lessons/string_and_list_methods.html")

@main_bp.route("/lessons/unit-8/dict_tuple_and_set_methods")
def dict_tuple_and_set_methods():
    return render_template("lessons/dict_tuple_and_set_methods.html")

@main_bp.route("/lessons/unit-8/file_methods_and_exceptions")
def file_methods_and_exceptions():
    return render_template("lessons/file_methods_and_exceptions.html")

@main_bp.route("/lessons/unit-9/built_in_and_math_modules")
def built_in_and_math_modules():
    return render_template("lessons/built_in_and_math_modules.html")

@main_bp.route("/lessons/unit-9/requests_module")
def requests_module():
    return render_template("lessons/requests_module.html")

@main_bp.route("/lessons/unit-10/how_to_basic_recipes")
def how_to_basic_recipes():
    return render_template("lessons/how_to_basic_recipes.html")




# QUIZZES
# ==========================================
# UNIT 1 QUIZZES
# ==========================================

@main_bp.route('/quizzes/unit1/basic-info')
def quiz_basic_info():
    return render_template('quizzes/unit1/01_basic_info.html')

@main_bp.route('/quizzes/unit1/variables')
def quiz_variables():
    return render_template('quizzes/unit1/02_variables.html')

@main_bp.route('/quizzes/unit1/types-and-numbers')
def quiz_types_numbers():
    return render_template('quizzes/unit1/03_types_numbers.html')

@main_bp.route('/quizzes/unit1/numbers-and-random')
def quiz_numbers_random():
    return render_template('quizzes/unit1/04_numbers_random.html')

@main_bp.route('/quizzes/unit1/strings')
def quiz_strings():
    return render_template('quizzes/unit1/05_strings.html')

@main_bp.route('/quizzes/unit1/booleans')
def quiz_booleans():
    return render_template('quizzes/unit1/06_booleans.html')

@main_bp.route('/quizzes/unit1/operators')
def quiz_operators():
    return render_template('quizzes/unit1/07_operators.html')

@main_bp.route('/quizzes/unit1/lists')
def quiz_lists():
    return render_template('quizzes/unit1/08_lists.html')

@main_bp.route('/quizzes/unit1/tuples')
def quiz_tuples():
    return render_template('quizzes/unit1/09_tuples.html')

@main_bp.route('/quizzes/unit1/sets')
def quiz_sets():
    return render_template('quizzes/unit1/10_sets.html')

@main_bp.route('/quizzes/unit1/dictionaries')
def quiz_dictionaries():
    return render_template('quizzes/unit1/11_dictionaries.html')

@main_bp.route('/quizzes/unit1/conditions')
def quiz_conditions():
    return render_template('quizzes/unit1/12_conditions.html')

@main_bp.route('/quizzes/unit1/loops')
def quiz_loops():
    return render_template('quizzes/unit1/13_loops.html')

@main_bp.route('/quizzes/unit1/functions')
def quiz_functions():
    return render_template('quizzes/unit1/14_functions.html')

@main_bp.route('/quizzes/unit1/sequences')
def quiz_sequences():
    return render_template('quizzes/unit1/15_sequences.html')

@main_bp.route('/quizzes/unit1/iterators-modules')
def quiz_iterators_modules():
    return render_template('quizzes/unit1/16_iterators_modules.html')

@main_bp.route('/quizzes/unit1/datetime-math-json')
def quiz_datetime_math_json():
    return render_template('quizzes/unit1/17_datetime_math_json.html')

@main_bp.route('/quizzes/unit1/regex')
def quiz_regex():
    return render_template('quizzes/unit1/18_regEx.html')

@main_bp.route('/quizzes/unit1/pip-exceptions')
def quiz_pip_exceptions():
    return render_template('quizzes/unit1/19_pip_exceptions.html')

@main_bp.route('/quizzes/unit1/string-formatting')
def quiz_string_formatting():
    return render_template('quizzes/unit1/20_string_formatting.html')

@main_bp.route('/quizzes/unit1/none-input-venv')
def quiz_none_input_venv():
    return render_template('quizzes/unit1/21_none_input_venv.html')


# ==========================================
# UNIT 2 & 3 QUIZZES
# ==========================================

@main_bp.route('/quizzes/unit2/oop')
def quiz_oop():
    return render_template('quizzes/unit2/01_oop.html')

@main_bp.route('/quizzes/unit3/file-handling')
def quiz_file_handling():
    return render_template('quizzes/unit3/01_file_handling.html')