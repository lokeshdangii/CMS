from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from db import db, cursor
from auth import login_required

# BluePrint
links = Blueprint('links',__name__)


# ------------------------------------- COLOR -----------------------------------------------------------------

# Route to display all Cars of Specific Colors
@links.route('/color_link/<int:color_id>')
@login_required
def color_table(color_id):
    cursor.execute("select ModelName, ColorName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarColor on Car.ColorID = CarColor.ColorID where CarColor.ColorID = %s", (color_id,))
    cars = cursor.fetchall()

    cursor.execute("select COUNT(*) ModelName, ColorName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID  inner join CarColor on Car.ColorID = CarColor.ColorID where CarColor.ColorID = %s", (color_id,))
    count = cursor.fetchone()
    return render_template('links/color.html', cars = cars, count = count)


# -------------------------------------  VARIANT  -----------------------------------------------------------

# Route to display all Cars of Specific Variant
@links.route('/variant_link/<int:variant_id>')
@login_required
def variant_table(variant_id):
    cursor.execute("select ModelName, VariantName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarVariant on Car.VariantID = CarVariant.VariantID where CarVariant.VariantID = %s", (variant_id,))
    cars = cursor.fetchall()

    cursor.execute("select COUNT(*) ModelName, VariantName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarVariant on Car.VariantID = CarVariant.VariantID where CarVariant.VariantID = %s", (variant_id,))
    count = cursor.fetchone()
    return render_template('links/variant.html', cars = cars, count = count)


# ------------------------------------- ENGINE -----------------------------------------------------------------

# Route to display all Cars of Specific Engine
@links.route('/engine_link/<int:engine_id>')
@login_required
def engine_table(engine_id):
    cursor.execute("select ModelName, EngineName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarEngine on Car.EngineID = CarEngine.EngineID where Car.EngineID = %s", (engine_id,))
    cars = cursor.fetchall()

    cursor.execute("select COUNT(*) ModelName, EngineName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarEngine on Car.EngineID = CarEngine.EngineID where Car.EngineID = %s", (engine_id,))
    count = cursor.fetchone()
    return render_template('links/engine.html', cars = cars, count = count)


# ------------------------------------- CATEGORY  -----------------------------------------------------------------

# Route to display all Cars of Specific Category
@links.route('/category_link/<int:category_id>')
@login_required
def category_table(category_id):
    cursor.execute("select ModelName, CategoryName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarCategory on Car.CategoryID = CarCategory.CategoryID where CarCategory.CategoryID = %s", (category_id,))
    cars = cursor.fetchall()

    cursor.execute("select COUNT(*) ModelName, CategoryName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID   inner join CarCategory on Car.CategoryID = CarCategory.CategoryID where CarCategory.CategoryID = %s", (category_id,))
    count = cursor.fetchone()
    return render_template('links/category.html', cars = cars, count = count)


# ------------------------------------- MODEL  -----------------------------------------------------------------

# Route to display all Cars of Specific Category
@links.route('/model_link/<int:model_id>')
@login_required
def model_table(model_id):
    cursor.execute("SELECT CarModel.ModelName, CarColor.ColorName, CarVariant.VariantName FROM Car INNER JOIN CarModel ON Car.ModelID = CarModel.ModelID INNER JOIN CarColor ON Car.ColorID = CarColor.ColorID inner join CarVariant on Car.VariantID = CarVariant.VariantID WHERE CarModel.ModelID =  %s", (model_id,))
    cars = cursor.fetchall()

    cursor.execute("select COUNT(*) ModelName, ModelName from CarModel inner join Car  on Car.ModelID = CarModel.ModelID  where Car.ModelID = %s", (model_id,))
    count = cursor.fetchone()
    return render_template('links/model.html', cars = cars, count = count)

