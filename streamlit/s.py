import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Функция для страницы 1

def page1():
    st.title("Раздел 1: Количество случаев ВЭБ (АБС_ВЭБ) для патологии ИМ")
    # Здесь можно разместить элементы страницы "Раздел 1"
    # Добавьте подписи обозначений
    st.markdown(" <span style='color:blueviolet'>Необходимо указать:</span>", unsafe_allow_html=True)
    st.write('N_ABS - число заболевших ИМ')
    # Запросить ввод пользователя
    N_ABS = st.number_input('Введите значение N_ABS', min_value=0)
    # Заданные коэффициенты
    st.markdown(" <span style='color:blueviolet'>Заданные коэффициенты:</span>", unsafe_allow_html=True)
    st.write('%_ВЭБ - доля случаев ИМ, вызванный ВЭБ = 0.9' )
    st.write('%_АМБ_ВЭБ - доля амбулаторных случаев ИМ = 0.1')
    st.write('%_СТАЦ_ВЭБ - доля стационарных случаев ИМ = 0.9')
    # Расчетные параметры
    st.markdown(" <span style='color:blueviolet'>Расчетные параметры:</span>", unsafe_allow_html=True)
    st.write('АБС_ВЭБ - число случаев ВЭБ среди ИМ')
    st.write('АМБ_АБС_ВЭБ - число случаев ИМ, амбулаторных')
    st.write('СТАЦ_АБС_ВЭБ - число случаев ИМ, стационарных')


    # Задать коэффициенты
    percent_VEB = 0.9
    percent_AMB_VEB = 0.1
    percent_STAC_VEB = 0.9

    # Вычислить значения
    VEB_ABS = N_ABS * percent_VEB
    AMB_VEB_ABS = (VEB_ABS * percent_AMB_VEB)
    STAC_VEB_ABS = (VEB_ABS * percent_STAC_VEB)

    # Отобразите результаты, округлить до целого
    st.write('АМБ_АБС_ВЭБ:', AMB_VEB_ABS)
    st.write('СТАЦ_АБС_ВЭБ:', STAC_VEB_ABS)

    # Создайте кнопку для перерисовки графика
    if st.button('Визуализировать график'):
        # Создайте Pie Chart
        fig, ax = plt.subplots()
        ax.set_title('Количество амбулаторных\n и стационарных случаев ВЭБ для патологии ИМ')
        ax.pie([AMB_VEB_ABS, STAC_VEB_ABS], colors=['blueviolet', 'cornflowerblue'], autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum([AMB_VEB_ABS, STAC_VEB_ABS])/100), labels=['АМБ_АБС_ВЭБ', 'СТАЦ_АБС_ВЭБ'])
        ax.axis('equal')

        # Добавьте Pie Chart в Streamlit
        st.pyplot(fig)

    st.title("Раздел 2:Прямые медицинские расходы")
    st.write("Расчет амбулаторных прямых медицинских расходов")

    st.markdown(" <span style='color:blueviolet'>Заданные коэффициенты:</span>", unsafe_allow_html=True)
    st.write('Стоимость случая лечения при госпитализации = 7641.77 рублей')
    st.markdown("Тариф на оплату случая ИМ по тарифу ФОМС =  <span style='color:red'>58303.56 рублей</span>",
                unsafe_allow_html=True)

    st.markdown(" <span style='color:blueviolet'>Рассчетные параметры:</span>", unsafe_allow_html=True)
    st.write('Амбулаторные ПМР')
    st.write('Стационарные ПМР')

    # Указать коэффициенты
    KLIM_MIN = 7641.77
    TFOMS_STAC = 58303.56


        # Вычисления
    AMB_PMR = AMB_VEB_ABS * KLIM_MIN
    STAC_PMR = STAC_VEB_ABS * TFOMS_STAC

        # Вывод результатов
    st.write('Амбулаторные ПМР_АМБ:', AMB_PMR)
    st.write('Стационарные ПМР_СТАЦ:', STAC_PMR)
    if st.button('График амбулаторных и стационарных ПМР'):
        # Создайте Pie Chart
        fig, ax = plt.subplots()
        ax.set_title('График амбулаторных и стационарных ПМР для патологии ИМ')
        ax.pie([AMB_PMR, STAC_PMR], colors=['mediumturquoise', 'mediumpurple'],
               autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum([AMB_VEB_ABS, STAC_VEB_ABS])/100),
               labels=['АМБ_ПМР', 'СТАЦ_ПМР'])
        ax.axis('equal')

        # Добавьте Pie Chart в Streamlit
        st.pyplot(fig)

    # Раздел 3
    st.title("Раздел 3:Непрямые потери экономики (НПЭ)")
    st.write("Расчет непрямых потерь экономики для взрослых диагнозов, когда пациент берет больничный")
    st.markdown(" <span style='color:blueviolet'>Необходимо указать:</span>", unsafe_allow_html=True)
    st.write('ВВП за год - значение ВВП за год, млрд рублей(151455.6)')
    ВВП_ГОД = st.number_input("Введите значение ВВП за год", min_value=0)
    st.write('ТРУД_НАС  - численность трудоспособного населения за год (83920207)')
    ТРУД_ЧИСЛ = st.number_input("Введите численность трудоспособного населения", min_value=0)
    st.write('ДОЛЯ_ТРУД  - доля рабочего населения (0.9963)')
    ДОЛЯ_ТРУД = st.number_input("Введите долю рабочего населения", min_value=0)
    # Заданные коэффициенты
    st.markdown(" <span style='color:blueviolet'>Заданные коэффициенты:</span>", unsafe_allow_html=True)
    st.write('Длительность заболевания  = 12 дней')
    ДЛИТ_ЗАБ = 12
    st.write('Доля больных трудоспособного возраста среди госпитализированных пациентов = 0.313')
    ДЛИТ_ТРУД_СРЕДИ_ГОСП = 0.313
    # Расчетные параметры
    st.markdown(" <span style='color:blueviolet'>Расчетные параметры:</span>", unsafe_allow_html=True)
    st.write('НП_ВЗРОСЛЫЙ - непрямые потери экономики по взрослым')
    NEPR_YSHCERB = 0

    # Вычисления
    ВВП_ДЕНЬ_ЧЕЛ = ВВП_ГОД / (ТРУД_ЧИСЛ * 365)
    НПЭ_ВЗРОС = STAC_VEB_ABS * ДЛИТ_ЗАБ * ВВП_ДЕНЬ_ЧЕЛ * ДЛИТ_ТРУД_СРЕДИ_ГОСП * ДОЛЯ_ТРУД

    # Вывод результатов
    st.write('НПЭ_ВЗРОС, млрд рублей:', НПЭ_ВЗРОС)

    # Раздел 4
    st.title("Раздел 4:Суммарный экономический ущерб")

    СУММ_ВЭБ = AMB_PMR + STAC_PMR + НПЭ_ВЗРОС
    st.write('Суммарный экономический ущерб, млрд рублей:', СУММ_ВЭБ)
    st.write('Прямой экономический ущерб, амбулаторный, млрд рублей:', AMB_PMR)
    st.write('Прямой экономический ущерб,стационарный, млрд рублей:', STAC_PMR)
    st.write('Непрямой экономический ущерб, млрд рублей:', НПЭ_ВЗРОС)

    # визуализировать структуру на графике СУММ_ВЭБ

    if st.button('График Структура Экономического ущерба'):
        # Создайте Pie Chart
        fig, ax = plt.subplots()
        ax.set_title('Структура Экономического ущерба')
        wedges, texts, autotexts = ax.pie([AMB_PMR, STAC_PMR, НПЭ_ВЗРОС],
                                          colors=['mediumturquoise', 'mediumpurple', 'lightcoral'],
                                          autopct=lambda p: '{:.2f}%'.format(p)
                                          )
        ax.axis('equal')

        # Добавьте легенду в правой нижней части
        ax.legend(wedges, ['АМБ_ПМР', 'СТАЦ_ПМР', 'НПЭ_ВЗРОС'],
                  title="Легенда",
                  loc="lower right")

        # Добавьте Pie Chart в Streamlit
        st.pyplot(fig)

# Функция для страницы 2




def page2():
    st.markdown(" <span style='color:blueviolet'>Заданные коэффициенты:</span>", unsafe_allow_html=True)


# Функция для страницы 3
def page3():
    st.title("Page 3")
    st.write("This is page 3")

# Функция для страницы 4
def page4():
    st.title("Page 4")
    st.write("This is page 4")

# Создание навигационного меню
page = st.sidebar.radio("Select a page", ["Расчет ЭУ (взрослые)", "Расчет ЭУ (дети)", "НПЭ", "Суммарный ЭУ"])

# Вызов соответствующей функции в зависимости от выбранной страницы
if page == "Расчет ЭУ (взрослые)":
    page1()
elif page == "Расчет ЭУ (дети)":
    page2()
elif page == "3 страница":
    page3()
elif page == "Суммарный ЭУ":
    page4()










