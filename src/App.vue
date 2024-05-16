<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-grey-4 text-black">
      <q-toolbar>
        <div class="row items-center justify-between">
          <div class="col-auto q-mr-lg q-ml-lg">
            <span class="text-h5">
              Мониторинг<br>микроклимата
            </span>
          </div>
          <q-space />
          <div class="col-auto">
            <q-tabs
              v-model="tab"
              class="text-black">
              <q-tab name="download" icon="download" label="Загрузка" />
              <q-tab name="graph" icon="show_chart" label="Графики" />
              <q-tab name="diagram" icon="bubble_chart" label="Диаграммы" />
              <q-tab name="heatmap" icon="layers" label="Тепловые карты" />
              <q-tab name="statistics" icon="bar_chart" label="Статистика" />
              <q-tab name="report" icon="description" label="Отчет" />
            </q-tabs>
          </div>
        </div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style>
/* Ваши стили */
</style>

<script>
import router from './router'
export default {
  name: 'App',
  router
}
</script>

