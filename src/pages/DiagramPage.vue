<template>
  <q-page padding>
    <div class="q-pa-md">
      <q-card>
        <q-card-section>
          <div class="row q-col-gutter-md items-center">
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
              @click="showChart"
              :disable="!selectedParameter || !selectedPeriod"
            />
          </div>
        </q-card-section>

        <div class="row q-col-gutter-md">
          <div class="col-6">
            <q-card-section>
              <canvas ref="chart" width="400" height="200"></canvas>
            </q-card-section>
          </div>
          <div class="col-6">
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
      parameters: [
        { label: 'Температура', value: 'temperature' },
        { label: 'Влажность', value: 'humidity' },
        { label: 'Уровень загрязнения', value: 'pollution' },
      ],
      periods: [
        { label: 'День', value: 'day' },
        { label: 'Неделя', value: 'week' },
        { label: 'Месяц', value: 'month' },
      ],
      chart: null,
      tableData: [],
      columns: [
        { name: 'timestamp', label: 'Единица периода измерения', field: 'timestamp', align: 'left' },
        { name: 'value', label: 'Значение', field: 'value', align: 'right' },
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
      // логика получения данных в зависимости от выбора в селектах
      return [
        { id: 1, timestamp: '2024-05-17', value: 40 },
        { id: 2, timestamp: '2024-05-18', value: 10 },
        { id: 2, timestamp: '2024-05-19', value: 5 },
        { id: 1, timestamp: '2024-05-20', value: 20 },
        { id: 2, timestamp: '2024-05-21', value: 30 },
        { id: 2, timestamp: '2024-05-22', value: 1 },
      ];
    },
    updateChart(data) {
      if (this.chart) {
        this.chart.destroy();
      }
      const ctx = this.$refs.chart.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: data.map(item => item.timestamp),
          datasets: [
            {
              label: 'Значение',
              data: data.map(item => item.value),
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
              ],
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
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
