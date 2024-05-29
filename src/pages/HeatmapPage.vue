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
            />
            <q-select
              v-model="selectedRegion"
              :options="regions"
              label="Район исследования"
              outlined
              class="col-6"
              style="max-width: 300px"
            />
            <q-btn
              label="Показать"
              color="light-green-14"
              class="q-ml-md q-mt-md q-pa-sm"
              @click="showHeatmap"
              style="max-height: 40px;"
              :disable="!selectedParameter || !selectedRegion"
            />
          </div>
        </q-card-section>

        <div class="row q-col-gutter-md justify-center">
          <div class="col-12 heatmap-container">
            <svg ref="heatmapSvg" width="900" height="600"></svg>
          </div>
        </div>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'HeatmapPage',
  data() {
    return {
      selectedParameter: null,
      selectedRegion: null,
      parameters: [
        { label: 'Температура', value: 'temperature' },
        { label: 'Влажность', value: 'humidity' },
        { label: 'Уровень загрязнения', value: 'pollution' },
      ],
      regions: [
        { label: 'Район 1 (30.00000; 39.99999)', value: {x: 30.00000, y: 39.99999} },
        { label: 'Район 2 (40.00000; 49.99999)', value: {x: 40.00000, y: 49.99999} },
        { label: 'Район 3 (50.00000; 59.99999)', value: {x: 50.00000, y: 59.99999} },
      ],
      heatmapData: [
        { x: 30.5010, y: 50.5489, value: 16 },
        { x: 30.8460, y: 50.4890, value: 24 },
        { x: 30.4389, y: 50.7542, value: 18 },
        { x: 30.5568, y: 50.7589, value: 20 },
        { x: 30.6543, y: 50.7645, value: 28 },
        { x: 30.5764, y: 50.4357, value: 12 },
      ],
      xDomain: [30.0, 31.0],  // Примерные координаты для оси X (долгота)
      yDomain: [50.0, 51.0],  // Примерные координаты для оси Y (широта)
    };
  },
  methods: {
    showHeatmap() {
      const heatmapSvg = d3.select(this.$refs.heatmapSvg);

      // Очистка предыдущей отрисовки
      heatmapSvg.selectAll('*').remove();

      // Настройки размеров и отступов
      const margin = { top: 50, right: 180, bottom: 50, left: 100 };
      const width = 800 - margin.left - margin.right;
      const height = 600 - margin.top - margin.bottom;

      // Группа для размещения осей и тепловой карты
      const g = heatmapSvg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      // Шкалы для осей
      const xScale = d3.scaleLinear()
        .domain(this.xDomain)
        .range([0, width]);

      const yScale = d3.scaleLinear()
        .domain(this.yDomain)
        .range([height, 0]);

      const colorScale = d3.scaleLinear()
        .domain([0, d3.max(this.heatmapData, d => d.value)])
        .range(['blue', 'red']);

      // Отрисовка прямоугольников для каждой точки данных
      g.selectAll('rect')
        .data(this.heatmapData)
        .enter()
        .append('rect')
        .attr('x', d => xScale(d.x))
        .attr('y', d => yScale(d.y))
        .attr('width', (width / (this.xDomain[1] - this.xDomain[0])) * 0.1)  // Примерный размер ячейки
        .attr('height', (height / (this.yDomain[1] - this.yDomain[0])) * 0.1) // Примерный размер ячейки
        .attr('fill', d => colorScale(d.value));

      // Добавление осей
      g.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(xScale).tickFormat(d => d.toFixed(2)));

      g.append('g')
        .call(d3.axisLeft(yScale).tickFormat(d => d.toFixed(2)));

      // Подписи осей
      g.append('text')
        .attr('text-anchor', 'end')
        .attr('x', width / 2)
        .attr('y', height + margin.top - 10)
        .text('Долгота');

      g.append('text')
        .attr('text-anchor', 'end')
        .attr('transform', 'rotate(-90)')
        .attr('x', -height / 2)
        .attr('y', -margin.left + 20)
        .text('Широта');

      // Добавление легенды
      const legend = heatmapSvg.append('g')
        .attr('transform', `translate(${width + margin.right - 50}, ${margin.top})`);

      legend.selectAll('rect')
        .data(colorScale.ticks(10).map(value => ({ value, color: colorScale(value) })))
        .enter()
        .append('rect')
        .attr('x', 0)
        .attr('y', (d, i) => i * 20)
        .attr('width', 20)
        .attr('height', 20)
        .attr('fill', d => d.color);

      legend.selectAll('text')
        .data(colorScale.ticks(10))
        .enter()
        .append('text')
        .attr('x', 25)
        .attr('y', (d, i) => i * 20 + 15)
        .text(d => Math.round(d));
    },
  },
};
</script>

<style scoped>
.heatmap-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
</style>
