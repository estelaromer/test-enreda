<template>
  <div class="content-container">
    <app-list-notes v-bind:notes="notes"></app-list-notes>
  </div>
</template>

<script>
import ListNotes from './ListNotes.vue'

export default {
  name: 'Content',
  components: {
    'app-list-notes': ListNotes
  },
  data () {
    return {
      notes: [
        {
          id: 1,
          endDate: '2020-07-20',
          note: 'Primera nota',
          userEmail: 'user1@example.com',
          task: false,
          tag: 'Factura, Julio'
        },
        {
          id: 2,
          endDate: '2020-07-21',
          note: 'Segunda nota',
          userEmail: 'user1@example.com',
          task: true,
          tag: 'Cita médica'
        },
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin: auto;
  padding: 4em;
}
</style>