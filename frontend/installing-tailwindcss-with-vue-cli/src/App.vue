<template>
  <div id="app">
    <div class="p-3 bg-green-500 text-white">Hello Tailwind CSS</div>

    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>

    <ul>
      <li v-for="(note, index) in notes" :key="index">
        <p>
          Post: {{note.content}}
        </p>
        <p>
          upvote: {{note.upvote}}
        </p>
        <p>
          downvote: {{note.downvote}}
        </p>
      </li>
    </ul>

    <input v-model="content"/>
    <button @click="submitNewNote">
      Submit
    </button>



    <router-view/>
  </div>
</template>


<script>
export default {
  name: 'App',
  props: {

  },
  data(){
    return{
      notes: [],
      content: '',
    }
  },
  mounted() {
    this.$http.get('notes/')
      .then((response) => {
        this.notes = response.data
        console.log(this.notes)
      })
  },
  methods: {
    submitNewNote(){
      this.$http.post(('notes/'),
          {content: this.content}
      ).then((response) => {
        console.log(response)
      })


    }
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
