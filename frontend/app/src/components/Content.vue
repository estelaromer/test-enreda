<template>
  <div class="content-container">
    <app-add-new-note v-bind:users="users" v-on:create-note="createNote"></app-add-new-note>
    <app-list-notes v-bind:notes="notes"></app-list-notes>
  </div>
</template>

<script>
import ListNotes from './ListNotes.vue'
import AddNewNote from './AddNewNote.vue'
import axios from 'axios'

export default {
  name: 'Content',
  components: {
    'app-list-notes': ListNotes,
    'app-add-new-note': AddNewNote
  },
  data () {
    return {
      notes: [],
      users: []
    }
  },
  methods: {
    createNote(note) {
      var newNote = new FormData()
      newNote.append('end_date', note.endDate)
      newNote.append('note', note.note)
      if (note.attachedFile !== null){
        newNote.append('attached_file', note.attachedFile)
      }
      
      newNote.append('user_email', note.userEmail)
      newNote.append('task', note.task)
      newNote.append('tag', (note.tag !== '') ? note.tag : null)
 
      // Add the new note to the database via a HTTP POST call
      axios.post('http://localhost:8000/api/notes/new/', newNote, {headers: {'Content-Type': 'multipart/form-data'}})
        .then((response) => {
          // handle success
          this.messageType = 'Success'
          this.messageToDisplay = 'SUCCESS! Note data was saved!'

          // Add the user to the local array of users
          this.notes.push(newNote);

          // Increase the largest index used in the database
          this.largestNoteIndex++
        })
        .catch((error) => {
          // handle error
          this.messageType = 'Error'
          this.messageToDisplay = 'ERROR! Unable to save note data!'
          console.log(error);
        })
        .finally((response) => {
          // always executed
          console.log('HTTP POST Finished!');
      // GET request for user data
      axios.get('http://localhost:8000/api/notes/')
        .then((response) => {
          // handle success
          console.log('Received response:');
          console.log(response);

          // Add the 'editing' field to each user object
          var mountedNotes = response.data.map(function (note) {
            // note.editing = false;
            let newNote = {
              id: note.id,
              date: note.date,
              endDate: note.end_date,
              note: note.note,
              userId: note.user_id,
              userName: note.user_name,
              userEmail: note.user_email,
              task: note.task,
              tag: note.tag
            }
            console.log(newNote);
            return newNote;
          })
          this.notes = mountedNotes;

          console.log('Notes array in success callback:');
          console.log(this.notes);
        })
        .catch((error) => {
          // handle error
          console.log(error);
          this.errorMessage = 'Error! Unable to load USER data!';
        })
        .finally((response) => {
          // always executed
          console.log('Finished!');
        });
  });
      
    }
  },
  beforeCreate() {
    console.log('Content.vue: beforeCreate() called!')
  },
  created() {
    // GET request for user data
    axios.get('http://localhost:8000/api/notes/')
      .then((response) => {
        // handle success
        console.log('Received response:');
        console.log(response);

        // Add the 'editing' field to each user object
        var mountedNotes = response.data.map(function (note) {
          // note.editing = false;
          let newNote = {
            id: note.id,
            date: note.date,
            endDate: note.end_date,
            note: note.note,
            userId: note.user_id,
            userName: note.user_name,
            userEmail: note.user_email,
            task: note.task,
            tag: note.tag
          }
          console.log(newNote);
          return newNote;
        })
        this.notes = mountedNotes;

        console.log('Notes array in success callback:');
        console.log(this.notes);
      })
      .catch((error) => {
        // handle error
        console.log(error);
        this.errorMessage = 'Error! Unable to load USER data!';
      })
      .finally((response) => {
        // always executed
        console.log('Finished!');
      });
  // GET request for user data
  axios.get('http://localhost:8000/api/notes/users/')
    .then((response) => {
      // handle success
      console.log('Received response:');
      console.log(response);

      // Add the 'editing' field to each user object
      var mountedUsers = response.data.map(function (user) {
        // note.editing = false;
        let newUser = {
          id: user.id,
          name: user.name,
          email: user.email,
        }
        console.log(newUser);
        return newUser;
      })
      this.users = mountedUsers;

      console.log('Users array in success callback:');
      console.log(this.users);
    })
    .catch((error) => {
      // handle error
      console.log(error);
      this.errorMessage = 'Error! Unable to load USER data!';
    })
    .finally((response) => {
      // always executed
      console.log('Finished!');
    });
  },
  beforeMount() {
    console.log('App.vue: beforeMount() called!')
  },
  mounted() {
    console.log('App.vue: mounted() called!')
  },
  beforeDestroy() {
    console.log('App.vue: beforeDestroy() called!')
  },
  destroyed() {
    console.log('App.vue: destroyed() called!')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin: auto;
  padding: 1em;
}
</style>