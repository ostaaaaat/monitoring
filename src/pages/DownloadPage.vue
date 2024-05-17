<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 400px; margin: auto;">
      <q-card>
        <q-card-section>
          <div class="text-h6 text-center">Загрузка файла</div>
        </q-card-section>
        <q-card-section align="center">
          <q-file
            v-model="file"
            label="Выберите файл"
            filled
            counter
            outlined
            clearable
            style="max-width: 300px"
          />
        </q-card-section>
        <q-card-actions align="center">
          <q-btn
            label="Загрузить"
            color="light-green-14"
            class="text-black"
            @click="uploadFile"
            :disable="!file"
          />
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'DownloadPage',
  data() {
    return {
      file: null,
    };
  },
  methods: {
    uploadFile() {
      if (this.file) {
        console.log('Загружаемый файл:', this.file);
      }
    },
  },
};
</script>

<style scoped>

</style>
