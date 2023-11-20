{% 
    set categories = var('food_list') 
%}

SELECT
    id,
    {% for category, foods in categories.items() %}
        {% for food in foods %}
            "{{food}}",
        {% endfor %}
    {% endfor %}
FROM fruit_veggie
