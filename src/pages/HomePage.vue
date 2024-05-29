<template>
    <q-page class="q-pa-md">
      <div class="text-h4 q-mb-md text-center">
        Добро пожаловать в систему мониторинга микроклимата!
      </div>
      <div class="row justify-center">
        <div class="col-4">
          <q-card class="q-mb-md q-ml-md" style="width: 30vw;">
            <q-card-section>
              <div class="row items-center">
                <div class="col-auto q-mr-md">
                  <q-icon name="show_chart" size="24px" />
                </div>
                <div class="col">
                  <div class="text-h6">Графики</div>
                  <div class="text-body1">Исследуйте температуру, влажность и другие параметры в разные периоды времени.</div>
                </div>
              </div>
            </q-card-section>
            <q-card-actions align="center">
              <q-btn label="Перейти" color="light-green-14" @click="navigateToGraphsPage" />
            </q-card-actions>
          </q-card>
        </div>
        <div class="col-4">
          <q-card class="q-mb-md q-ml-md" style="width: 30vw;">
            <q-card-section>
              <div class="row items-center">
                <div class="col-auto q-mr-md">
                  <q-icon name="bubble_chart" size="24px" />
                </div>
                <div class="col">
                  <div class="text-h6">Диаграммы</div>
                  <div class="text-body1">Сравните различные показатели погоды с помощью наглядных диаграмм.</div>
                </div>
              </div>
            </q-card-section>
            <q-card-actions align="center">
              <q-btn label="Перейти" color="light-green-14" @click="navigateToDiagramsPage" />
            </q-card-actions>
          </q-card>
        </div>
        <div class="col-4">
          <q-card class="q-mb-md q-ml-md" style="width: 30vw;">
            <q-card-section>
              <div class="row items-center">
                <div class="col-auto q-mr-md">
                  <q-icon name="layers" size="24px" />
                </div>
                <div class="col">
                  <div class="text-h6">Тепловые карты</div>
                  <div class="text-body1">Получите наглядное представление о распределении параметров в различных районах.</div>
                </div>
              </div>
            </q-card-section>
            <q-card-actions align="center">
              <q-btn label="Перейти" color="light-green-14" @click="navigateToHeatmapsPage" />
            </q-card-actions>
          </q-card>
        </div>
      </div>
      <div class="col-4">
          <q-card class="q-mb-md q-ml-md" style="width: full-width;">
            <q-card-section>
              <div class="row items-center">
                <div class="col">
                  <div class="text-h6 text-center">Статистический анализ</div>
                  <div class="text-body1 text-center">Получите обзорные и детальные статистические данные, которые помогут вам выявить тренды, закономерности и аномалии в изменениях микроклимата. 
                    <br>Оцените статистические характеристики данных, включая среднее значение, медиану, стандартное отклонение и другие ключевые параметры, чтобы принимать обоснованные решения и планировать будущие действия.</div>
                </div>
              </div>
            </q-card-section>
          </q-card>
        </div>
      <div class="text-center">
        <q-btn label="Начать использование" color="light-green-14" @click="startUsing" />
      </div>
    </q-page>
  </template>
  
  <style scoped>
  </style>
  
  <script>
  export default {
    methods: {
      startUsing() {
        this.$router.push({ name: 'Download' });
      },
      navigateToGraphsPage() {
        this.$router.push({ name: 'Graph' });
      },
      navigateToDiagramsPage() {
        this.$router.push({ name: 'Diagram' });
      },
      navigateToHeatmapsPage() {
        this.$router.push({ name: 'Heatmap' });
      },
    },
  };
  </script>
  