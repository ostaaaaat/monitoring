<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-grey-4 text-black">
      <q-toolbar>
        <div class="row items-center justify-between">
          <div class="col-auto q-mr-lg q-ml-lg" @click="goToHome">
            <span class="text-h5 cursor-pointer">
              Мониторинг<br>микроклимата
            </span>
          </div>
          <div class="col-auto">
            <q-btn-group flat>
              <q-btn class="q-px-sm" icon="download" label="Загрузка" @click="$router.push({ name: 'Download' })" />
              <q-btn class="q-px-sm" icon="show_chart" label="Графики" @click="$router.push({ name: 'Graph' })" />
              <q-btn class="q-px-sm" icon="bubble_chart" label="Диаграммы" @click="$router.push({ name: 'Diagram' })" />
              <q-btn class="q-px-sm" icon="layers" label="Тепловые карты" @click="$router.push({ name: 'Heatmap' })" />
            </q-btn-group>
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

</style>

<script>
export default {
  name: 'App',
  methods: {
    goToHome() {
      this.$router.push({ name: 'Home' });
    }
  }
}
</script>

