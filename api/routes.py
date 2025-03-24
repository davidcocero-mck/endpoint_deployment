import os
import pandas as pd
import uuid
from flask import Blueprint, jsonify, request
import time
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
    result = {
            "input": {
                "chat_history": [["user", "Hey"], ["assistant", "how can I help you?"]],
                "chat_input": "Cuál fue el EBITDA en Agosto de 2024 comparado con Julio?",
            },
            "llm_answer": """<body><table id="data-table">
                <thead>
                    <tr>
                        <th>Indicador</th>
                        <th>Valor</th>
                        <th>Cambio</th>
                    </tr>
                </thead>
                <tbody>

        <tr data-level="0" data-id="ebitda_chile" >
            <td><span class="toggle-icon"></span> ebitda_chile</td>
            <td>45.1M CLP</td>
            <td>1.6M CLP (3.7%)</td>
        </tr>

        <tr data-level="1" data-id="margen_de_contribucion" data-parent="ebitda_chile">
            <td><span class="toggle-icon"></span> &nbsp;&nbsp;&nbsp;margen_de_contribucion</td>
            <td>76.8M CLP</td>
            <td>2.8M CLP (3.7%)</td>
        </tr>

        <tr data-level="2" data-id="margen_de_contribucion_b2c" data-parent="margen_de_contribucion">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;margen_de_contribucion_b2c</td>
            <td>54.0M CLP</td>
            <td>4.8M CLP (9.7%)</td>
        </tr>

        <tr data-level="2" data-id="margen_de_contribucion_b2b" data-parent="margen_de_contribucion">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;margen_de_contribucion_b2b</td>
            <td>21.7M CLP</td>
            <td>4.1M CLP (23.6%)</td>
        </tr>

        <tr data-level="2" data-id="margen_de_contribucion_b2b_digital" data-parent="margen_de_contribucion">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;margen_de_contribucion_b2b_digital</td>
            <td>2.2M CLP</td>
            <td>-611.8K CLP (-21.6%)</td>
        </tr>

        <tr data-level="2" data-id="margen_de_contribucion_mayoristas" data-parent="margen_de_contribucion">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;margen_de_contribucion_mayoristas</td>
            <td>-1.1M CLP</td>
            <td>-5.5M CLP (-123.5%)</td>
        </tr>

        <tr data-level="1" data-id="costos_operacionales" data-parent="ebitda_chile">
            <td><span class="toggle-icon"></span> &nbsp;&nbsp;&nbsp;costos_operacionales</td>
            <td>-18.6M CLP</td>
            <td>2.7M CLP (-12.6%)</td>
        </tr>

        <tr data-level="2" data-id="arriendo_de_infraestructura_y_redes" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arriendo_de_infraestructura_y_redes</td>
            <td>4.2M CLP</td>
            <td>533.0K CLP (14.7%)</td>
        </tr>

        <tr data-level="2" data-id="arriendo_de_terrenos" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arriendo_de_terrenos</td>
            <td>4.7M CLP</td>
            <td>636.0K CLP (15.7%)</td>
        </tr>

        <tr data-level="2" data-id="oym_de_redes" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;oym_de_redes</td>
            <td>6.3M CLP</td>
            <td>2.0M CLP (46.3%)</td>
        </tr>

        <tr data-level="2" data-id="serv_profes_y_mantenc_hw_y_sw_sistema" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serv_profes_y_mantenc_hw_y_sw_sistema</td>
            <td>1.1M CLP</td>
            <td>236.2K CLP (26.9%)</td>
        </tr>

        <tr data-level="2" data-id="costos_personal_sistemas" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;costos_personal_sistemas</td>
            <td>977.6K CLP</td>
            <td>221.2K CLP (29.2%)</td>
        </tr>

        <tr data-level="2" data-id="otros_costos_operacionales" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;otros_costos_operacionales</td>
            <td>1.1M CLP</td>
            <td>-171.8K CLP (-13.4%)</td>
        </tr>

        <tr data-level="2" data-id="otros_costos_redes" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;otros_costos_redes</td>
            <td>891.0K CLP</td>
            <td>216.2K CLP (32.0%)</td>
        </tr>

        <tr data-level="2" data-id="servicios_de_ing_seg_y_com" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;servicios_de_ing_seg_y_com</td>
            <td>570.0K CLP</td>
            <td>154.1K CLP (37.1%)</td>
        </tr>

        <tr data-level="2" data-id="electricidad_redes" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;electricidad_redes</td>
            <td>-1.2M CLP</td>
            <td>-5.1M CLP (-130.8%)</td>
        </tr>

        <tr data-level="2" data-id="costos_almacenajetransporte" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;costos_almacenajetransporte</td>
            <td>447.8K CLP</td>
            <td>-185.7K CLP (-29.3%)</td>
        </tr>

        <tr data-level="2" data-id="otros_costos_sistemas" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;otros_costos_sistemas</td>
            <td>263.2K CLP</td>
            <td>-198.5K CLP (-43.0%)</td>
        </tr>

        <tr data-level="2" data-id="_arriendo_terrenos" data-parent="costos_operacionales">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_arriendo_terrenos</td>
            <td>-7.0M CLP</td>
            <td>-1.5M CLP (26.1%)</td>
        </tr>

        <tr data-level="1" data-id="gastos_administrativos" data-parent="ebitda_chile">
            <td><span class="toggle-icon"></span> &nbsp;&nbsp;&nbsp;gastos_administrativos</td>
            <td>-13.2M CLP</td>
            <td>-3.8M CLP (41.1%)</td>
        </tr>

        <tr data-level="2" data-id="bonos_e_indemnizaciones" data-parent="gastos_administrativos">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bonos_e_indemnizaciones</td>
            <td>7.6M CLP</td>
            <td>3.2M CLP (74.4%)</td>
        </tr>

        <tr data-level="2" data-id="costo_interno_rrhh" data-parent="gastos_administrativos">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;costo_interno_rrhh</td>
            <td>1.8M CLP</td>
            <td>1.0M CLP (127.8%)</td>
        </tr>

                </tbody>
            </table><script src="script.js"></script> </body>""",
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
            "chart": [{"type": "N/A", "code": "N/A", "id": "mychart"}],
            "complete": False,
        }
    response = {"predictions": result}
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
	time.sleep(10)
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
                    "id": str(uuid.uuid4()),
                }
            ],
            "complete": False,
        }
        response = {"predictions": result}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@api.route("/reasoning_why_debug", methods=["POST"])
def reasoning_why_debug():
    data = request.get_json()
    data_proc = pd.DataFrame([data])
    result = {
            "input": {
                "chat_history": [["user", "Hey"], ["assistant", "how can I help you?"]],
                "chat_input": "Cuál fue el EBITDA en Agosto de 2024 comparado con Julio?",
            },
            "llm_answer": """<body><h2>Comparación de las Adiciones Netas de M2M en 2024 con el Plan</h2>
El <b>adiciones netas M2M</b> decreció un <span class="red">-45.8%</span> (-167,839 usuarios) respecto al plan principalmente a causa de:
<ul>
    <li>Una disminución en las <span class="driver">ventas brutas</span> de <span class="red">-28.5%</span> (-141,129.9 usuarios), lo cual se debe completamente a la caída en las <span class="driver">ventas brutas excluyendo portabilidad</span> de <span class="red">-28.5%</span> (-141,129.9 usuarios).</li>
    <li>Un aumento en el <span class="driver">churn</span> de <span class="red">-17.9%</span> (-23,121.1 usuarios), que es totalmente atribuible al incremento en el <span class="driver">churn excluyendo portabilidad</span> de <span class="red">-17.9%</span> (-23,121.1 usuarios).</li>
</ul>


            <table id="data-table">
                <thead>
                    <tr>
                        <th>Indicador</th>
                        <th>2024 (real) (usuarios)</th><th>2024 (plan) (usuarios)</th><th>Diferencia (usuarios)</th><th>2023 (real)(usuarios)</th><th>Differencia (usuarios)</th>
                    </tr>
                </thead>
                <tbody>

        <tr data-level="0" data-id="adiciones netas m2mgps" >
            <td><span class="toggle-icon"></span> Adiciones Netas M2Mgps</td>
            <td>198981.0</td>
            <td>366820.0</td>
            <td>-167839.0 (<span class="red">-45.80%</span>)</td>
             <td>252469.0</td>
            <td>-53488.0 (<span class="red">-21.20%</span>)</td>

        </tr>

        <tr data-level="1" data-id="ventas brutas" data-parent="adiciones netas m2mgps">
            <td><span class="toggle-icon"></span> &nbsp;&nbsp;&nbsp;Ventas Brutas</td>
            <td>354797.0</td>
            <td>495926.9</td>
            <td>-141129.9 (<span class="red">-28.50%</span>)</td>
             <td>388349.0</td>
            <td>-33552.0 (<span class="red">-8.60%</span>)</td>

        </tr>

        <tr data-level="2" data-id="ventas brutas excluyendo portabilidad" data-parent="ventas brutas">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ventas Brutas Excluyendo Portabilidad</td>
            <td>354797.0</td>
            <td>495926.9</td>
            <td>-141129.9 (<span class="red">-28.50%</span>)</td>
             <td>388349.0</td>
            <td>-33552.0 (<span class="red">-8.60%</span>)</td>

        </tr>

        <tr data-level="1" data-id="churn" data-parent="adiciones netas m2mgps">
            <td><span class="toggle-icon"></span> &nbsp;&nbsp;&nbsp;Churn</td>
            <td>-152348.0</td>
            <td>-129226.9</td>
            <td>-23121.1 (<span class="red">-17.90%</span>)</td>
             <td>-135750.0</td>
            <td>-16598.0 (<span class="red">-12.20%</span>)</td>

        </tr>

        <tr data-level="2" data-id="churn excluyendo portabilidad" data-parent="churn">
            <td><span class="toggle-icon empty"></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Churn Excluyendo Portabilidad</td>
            <td>-152348.0</td>
            <td>-129226.9</td>
            <td>-23121.1 (<span class="red">-17.90%</span>)</td>
             <td>-135750.0</td>
            <td>-16598.0 (<span class="red">-12.20%</span>)</td>

        </tr>

                </tbody>
            </table>
            <script src='script.js'></script>
        </body>""",
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
            "chart": [{"type": "N/A", "code": "N/A", "id": "mychart"}],
            "complete": False,
        }
    response = {"predictions": result}
    return jsonify(response), 200


