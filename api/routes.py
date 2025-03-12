import os
import pandas as pd
from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200

@api.route("/follow_up", methods=["POST"])
def follow_up():
    """
    API endpoint to get model predictions.
    Expects JSON input with required fields.
    """
    try:
        data = request.get_json()
        data_proc = pd.DataFrame([data])
        result = ["Como se desglosó por Negocio?","Como es la descomposicion por Segmento?"]
        response = {"predictions": result}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@api.route("/reasoning_why", methods=["POST"])
def reasoning_why():
    data = request.get_json()
    data_proc = pd.DataFrame([data])
    response = {"predictions": """<table id="data-table">
    <thead>
      <tr>
        <th>Indicador</th>
        <th>Valor</th>
        <th>Cambio</th>
      </tr>
    </thead>
    <tbody>
      <!-- Top level row with children -->
      <tr data-level="0">
        <td>
          <span class="toggle-icon"></span>
          <span class="cell-text">Ingresos</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <!-- Child row with children -->
      <tr data-level="1">
        <td>
          <span class="toggle-icon"></span>
          <span class="cell-text">Servicios</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <!-- Grandchild rows -->
      <tr data-level="2">
        <td>
          <!-- No toggle icon for a row with no children -->
          <span class="toggle-icon empty"></span>
          <span class="cell-text">Hogar</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <tr data-level="2">
        <td>
          <span class="toggle-icon empty"></span>
          <span class="cell-text">Móvil</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <!-- Sibling of Servicios -->
      <tr data-level="1">
        <td>
          <span class="toggle-icon empty"></span>
          <span class="cell-text">Equipos</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <!-- Another top-level row with children -->
      <tr data-level="0">
        <td>
          <span class="toggle-icon"></span>
          <span class="cell-text">Costos</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <!-- Child rows -->
      <tr data-level="1">
        <td>
          <span class="toggle-icon empty"></span>
          <span class="cell-text">Operativo</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <tr data-level="1">
        <td>
          <span class="toggle-icon empty"></span>
          <span class="cell-text">Comercial</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
      <tr data-level="1">
        <td>
          <span class="toggle-icon empty"></span>
          <span class="cell-text">Admin</span>
        </td>
        <td>$999</td>
        <td>+9M (9%)</td>
      </tr>
    </tbody>
  </table>
	<script src="script.js"></script>"""}
    return jsonify(response), 200

@api.route("/predict", methods=["POST"])
def predict():
    """
    API endpoint to get model predictions.
    Expects JSON input with required fields.
    """
    try:
        data = request.get_json()
        data_proc = pd.DataFrame([data])
        result = {
            "input": {
                "chat_history": [["user", "Hey"], ["assistant", "how can I help you?"]],
                "chat_input": "Cuál fue el EBITDA en Agosto de 2024 comparado con Julio?",
            },
            "llm_answer": '<body>\n    <h2>Comparación del EBITDA  en 2024</h2>\n    <table>\n        <thead>\n            <tr>\n                <th>Mes</th>\n                <th>EBITDA (CLP)</th>\n                <th>Diferencia (%)</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>Julio 2024</td>\n                <td>41.982.068</td>\n                <td>-</td>\n            </tr>\n            <tr>\n                <td>Agosto 2024</td>\n                <td>44.919.508</td>\n                <td>7,0%</td>\n            </tr>\n        </tbody>\n    </table>\n</body><ul>\n<li>El crecimiento del <b>7.0%</b> en el EBITDA de agosto en comparación con julio sugiere una <b>tendencia positiva</b> en la rentabilidad de , lo que podría indicar una <b>mejora en la eficiencia operativa</b> o un aumento en la demanda de sus servicios.</li>\n<li>Este aumento en el EBITDA podría ser un indicativo de que las <b>estrategias de marketing</b> o promociones implementadas en julio están dando resultados, lo que podría ser un punto a considerar para futuras campañas.</li>\n<li>La diferencia en EBITDA entre los dos meses podría ser utilizada para <b>evaluar el impacto de factores externos</b>, como cambios en la regulación del sector o condiciones económicas, que podrían estar influyendo en el desempeño financiero de la empresa.</li>\n<li>Un análisis más profundo de los <b>costos operativos</b> en julio y agosto podría revelar áreas donde  ha logrado <b>reducir gastos</b> o mejorar su margen de beneficio, lo que sería valioso para la planificación financiera futura.</li>\n</ul><canvas id="69071060-4fa3-416e-95b6-58c00ccf11d4" width="649" height="482" style="display: block; box-sizing: border-box; height: 482px; width: 649px;"></canvas>',
            "intermediate_results": [
                {
                    "type": "parsed_question",
                    "format": "markdown",
                    "value": "¿Cuál fue el EBITDA en agosto de 2024 comparado con julio de 2024?",
                    "name": "parsed_question_1",
                    "show": False,
                },
                {
                    "type": "parsed_question",
                    "format": "markdown",
                    "value": "¿Cuál fue el EBITDA en agosto de 2024 comparado con julio de 2024?",
                    "name": "parsed_question_2",
                    "show": False,
                },
                {
                    "type": "product_mapping",
                    "format": "json",
                    "value": "{}",
                    "name": "product_mapping",
                    "show": False,
                },
                {
                    "type": "entity_recognition",
                    "format": "json",
                    "value": '{"completeness": "True", "response": "La pregunta es espec\\u00edfica y tiene toda la informaci\\u00f3n necesaria para ser respondida, ya que menciona el EBITDA  en dos meses espec\\u00edficos: julio y agosto de 2024.", "workflow": "what"}',
                    "name": "entity_recognition",
                    "show": False,
                },
                {
                    "type": "sql_queries",
                    "format": "sql",
                    "value": "{\"query_1\": \"SELECT \\n  SUM(CASE WHEN Year = 2024 AND Month = 8 THEN value END) AS EBITDA_August_2024,\\n  SUM(CASE WHEN Year = 2024 AND Month = 7 THEN value END) AS EBITDA_July_2024\\nFROM _nmc\\nWHERE LINEA_N1 = 'ebitda' AND Type = 'real';\"}",
                    "name": "SQL queries",
                    "show": True,
                },
                {
                    "type": "intermediate_executions",
                    "format": "markdown",
                    "value": "[(44919508.0, 41982068.0)]",
                    "name": "SQL queries",
                    "show": True,
                },
                {
                    "type": "response",
                    "format": "markdown",
                    "value": "**Comparación del EBITDA de  en 2024:**\n\n- **Agosto 2024: CLP 44,919,508**\n- **Julio 2024: CLP 41,982,068**\n\n**Diferencia:**\n- El EBITDA en agosto de 2024 fue **7.0%** mayor que en julio de 2024.",
                    "name": "SQL Agent response",
                    "show": False,
                },
            ],
            "prompt": "N/A",
            "guardrails": [{"flagged": False, "reason": "N/A", "type": "N/A"}],
            "sources": [
                {
                    "name": "",
                    "content": "",
                    "link": "",
                    "description": "",
                    "show": False,
                    "score": 0.0,
                }
            ],
            "resources": [
                {
                    "name": "",
                    "content": "",
                    "link": "",
                    "description": "",
                    "show": False,
                    "score": 0.0,
                }
            ],
            "chart": [
                {
                    "type": "bar",
                    "code": '{"type": "bar", "data": {"labels": ["Julio 2024", "Agosto 2024"], "datasets": [{"data": [41982068, 44919508], "backgroundColor": "#4472c4", "borderColor": "#4472c4", "borderWidth": 1, "barPercentage": 0.65, "borderRadius": 2}]}, "options": {"indexAxis": "x", "responsive": true, "maintainAspectRatio": false, "plugins": {"legend": {"display": false}}, "scales": {"y": {"beginAtZero": true, "title": {"display": true, "text": "CLP", "font": {"size": 14}}, "border": {"display": false, "dash": [10, 10], "dashOffset": 10}, "grid": {"color": "#00000025"}, "ticks": {"padding": 24}}, "x": {"display": true, "grid": {"display": false}}}}}',
                    "id": "69071060-4fa3-416e-95b6-58c00ccf11d4",
                }
            ],
            "complete": False,
        }
        response = {"predictions": result}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

