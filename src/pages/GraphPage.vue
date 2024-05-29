<template>
  <q-page >
    <div class="q-pa-sm">
      <q-card>
        <q-card-section>
          <div class="row q-col-gutter-md items-top">
            <q-date
              v-model="selectedDateRange"
              range
              label="Диапазон дат"
              outlined
              color="light-green-14"
              class="col-4 q-ml-md q-mt-md q-pa-xs"
              minimal
              style="max-width: 260px; max-height: 280px;"
              @input="showChart"
            />
            <q-select
              v-model="selectedParameter"
              :options="parameters"
              label="Параметр"
              outlined
              class="col-4"
              style="max-width: 300px"
              @input="showChart"
            />
            <q-select
              v-model="selectedPeriod"
              :options="periods"
              label="Период измерения"
              outlined
              class="col-4"
              style="max-width: 300px"
              @input="showChart"
            />
            <q-btn
              label="Показать"
              color="light-green-14"
              class="q-ml-md q-mt-md q-pa-sm"
              style="max-height: 40px;"
              @click="showChart"
              :disable="!selectedParameter || !selectedPeriod || !selectedDateRange"
            />
          </div>
        </q-card-section>
        <div class="row q-col-gutter-md">
          <div class="col-8">
            <q-card-section>
              <canvas ref="chart" width="400" height="200"></canvas>
            </q-card-section>
          </div>
          <div class="col-4">
            <q-card-section>
              <q-table :rows="tableData" :columns="columns" row-key="id" hide-bottom />
            </q-card-section>
          </div>
        </div>
      </q-card>
    </div>
    <q-card class="q-ma-sm">
    <div class="row q-col-gutter-sm">
          <div class="col-4">
            <q-card-section>
              <q-table :rows="statisticsData" :columns="col_stat" row-key="id" hide-bottom />
            </q-card-section>
          </div>
          <div class="col-8">
            <q-card-section class="text-center">
              <div class="text-h5">Результаты анализа</div>
              <div class="text-body1 q-mt-sm">
                После сравнения полученных результатов с нормами, можно сделать вывод...
              </div>
            </q-card-section>
          </div>
    </div>
    </q-card>
  </q-page>
</template>

<script>
import { Chart } from 'chart.js/auto';

export default {
  name: 'GraphPage',
  data() {
    return {
      selectedParameter: null,
      selectedPeriod: null,
      selectedDateRange: null,
      parameters: [
        { label: 'Температура', value: 'temperature' },
        { label: 'Влажность', value: 'humidity' },
        { label: 'Уровень загрязнения', value: 'pollution' },
      ],
      periods: [
        { label: 'Дни', value: 'day' },
        { label: 'Месяцы', value: 'month' },
        { label: 'Годы', value: 'year' },
      ],
      chart: null,
      tableData: [],
      columns: [
        { name: 'timestamp', label: 'Единица периода измерения', field: 'timestamp', align: 'left' },
        { name: 'value', label: 'Значение', field: 'value', align: 'right' },
      ],
      col_stat: [
        { name: 'mean', label: 'Среднее значение', field: 'mean', align: 'center' },
        { name: 'median', label: 'Медиана', field: 'median', align: 'center' },
        { name: 'stDeviation', label: 'Стандартное отклонение', field: 'stDeviation', align: 'center' },
        { name: 'abnormal', label: 'Аномальные значения', field: 'abnormal', align: 'center' },
      ],
      statisticsData: [
        {mean: 25.6, median: 24, stDeviation: 2.5, abnormal: 3 },
      ],
    };
  },
  methods: {
    showChart() {
      const data = this.getData();
      this.updateChart(data);
      this.tableData = data;
    },
    getData() {
      return [
        {  timestamp: '2024-05-17', value: 22 },
        {  timestamp: '2024-05-18', value: 40 },
        {  timestamp: '2024-05-19', value: 20 },
        {  timestamp: '2024-05-20', value: 5 },
        {  timestamp: '2024-05-21', value: 25 },
        {  timestamp: '2024-05-22', value: 17 },
      ];
    },
    updateChart(data) {
      if (this.chart) {
        this.chart.destroy();
      }
      const ctx = this.$refs.chart.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: data.map(item => item.timestamp),
          datasets: [
            {
              label: 'Значение',
              data: data.map(item => item.value),
              borderColor: 'rgba(127, 255, 0)',
              backgroundColor: 'rgba(50, 205, 50)',
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              title: {
                display: true,
                text: 'Дата',
              },
            },
            y: {
              title: {
                display: true,
                text: 'Значение',
              },
              beginAtZero: true,
            },
          },
        },
      });
    },
  },
  mounted() {
    this.showChart();
  },
};
</script>

<style scoped>

</style>
