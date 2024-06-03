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
            class="text-white"
            @click="uploadFile"
            :disable="!file"
          />
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import api from '@/api';

export default {
  name: 'DownloadPage',
  data() {
    return {
      file: null,
    };
  },
  methods: {
    async uploadFile() {
      if (this.file) {
        try {
          const response = await api.uploadCsv(this.file);
          console.log('Файл успешно загружен:', response);
          this.file = null;
        } catch (error) {
          console.error('Ошибка при загрузке файла:', error);
        }
      }
    },
  },
};
</script>

<style scoped>

</style>
