<template>
  <div class="content-container">
    <app-add-new-note v-on:create-note="createNote"></app-add-new-note>
    <app-list-notes v-bind:notes="notes"></app-list-notes>
  </div>
</template>

<script>
import ListNotes from './ListNotes.vue'
import AddNewNote from './AddNewNote.vue'

export default {
  name: 'Content',
  components: {
    'app-list-notes': ListNotes,
    'app-add-new-note': AddNewNote
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
  },
  methods: {
    createNote(note) {
      var newNote = {
        id: this.notes.length + 1,
        endDate: note.endDate,
        note: note.note,
        userEmail: note.userEmail,
        task: note.task,
        tag: note.tag
      }

      // Add the user to the local array of users
      this.notes.push(newNote);
      
    },
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