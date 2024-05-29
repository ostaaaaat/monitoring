<template>
  <q-page>
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
              class="col-6"
              style="max-width: 300px"
              @input="showChart"
            />
            <q-select
              v-model="selectedPeriod"
              :options="periods"
              label="Период измерения"
              outlined
              class="col-6"
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
        { name: 'value', label: 'Значение', field: 'value', align: 'left' },
        { name: 'count', label: 'Количество', field: 'count', align: 'right' },
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
        {value: 20, count: 5 },
        {value: 25, count: 4 },
        {value: 23, count: 9 },
        {value: 24, count: 3 },
        {value: 28, count: 6 },

      ];
    },
    updateChart(data) {
      if (this.chart) {
        this.chart.destroy();
      }
      const ctx = this.$refs.chart.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'scatter',
        data: {
          datasets: [{
            label: 'Частота появления величины',
            data: data.map(item => ({ x: item.value, y: item.count })),
            backgroundColor: 'rgba(50, 205, 50)',
          }],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              type: 'linear',
              title: {
                display: true,
                text: 'Значение показателя'
              }
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Количество раз'
              }
            }
          }
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
