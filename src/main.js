import { createApp } from 'vue'
import App from './App.vue'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import 'quasar/dist/quasar.css';
import '@quasar/extras/material-icons/material-icons.css';
import router from './router'

createApp(App).use(Quasar, quasarUserOptions).mount('#app').use(router)

