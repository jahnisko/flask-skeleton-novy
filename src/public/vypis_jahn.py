from flask import Blueprint,render_template
from .views import blueprint
@blueprint.route('/vypis_jahn', methods=['GET'])
def Vypis_jahn():
        pole=[[0,1],[2,3],[0,30]]
        pole[0][1]=pole[0][1]+1
        return render_template("public/views_jahn.tmpl", data = pole)
