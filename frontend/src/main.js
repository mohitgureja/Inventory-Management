import {createApp} from 'vue'
import {createPinia} from 'pinia'
import App from './App.vue'
import router from './router'
import '@mdi/font/css/materialdesignicons.css'; // Import MDI font

import 'vuetify/styles'
import {createVuetify} from "vuetify";
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components, directives,
    icons: {
        iconfont: 'mdi',
    },
});

const app = createApp(App)
const pinia = createPinia()
app.use(router)
app.use(pinia)
app.use(vuetify).mount("#app")