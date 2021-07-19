<template>
  <div id="app">
    <nav class="relative flex flex-wrap items-center justify-between px-2 py-3 bg-pink-500 mb-3">
      <div class="container px-4 mx-auto flex flex-wrap items-center justify-between">
        <div class="w-full relative flex justify-between lg:w-auto  px-4 lg:static lg:block lg:justify-start">
          <a class="text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white"
             href="#pablo">
            Bulletin of Noobs @ NKU CS
            <span v-if="is_login">| Welcome Noob Akiyama</span>
          </a>
          <button
              class="cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
              type="button">
            <span class="block relative w-6 h-px rounded-sm bg-white"></span>
            <span class="block relative w-6 h-px rounded-sm bg-white mt-1"></span>
            <span class="block relative w-6 h-px rounded-sm bg-white mt-1"></span>
          </button>
        </div>
        <div class="lg:flex flex-grow items-center" id="example-navbar-warning">
          <ul class="flex flex-col lg:flex-row list-none ml-auto">
            <li class="nav-item">
              <a class="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75"
                 href="#pablo">
                <i class="fab fa-facebook-square text-lg leading-lg text-white opacity-75"/><span
                  class="ml-2">Share</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75"
                 href="#pablo">
                <i class="fab fa-twitter text-lg leading-lg text-white opacity-75"/><span class="ml-2">Tweet</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75"
                 href="#pablo">
                <i class="fab fa-pinterest text-lg leading-lg text-white opacity-75"/><span class="ml-2">Pin</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>


    <ul style="text-align: center">
      <li v-for="(note, index) in notes" :key="index">
        <br>
        <div class="p-7 max-w-lg mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4">
          <div class="text-xl font-medium text-black">{{ note.username }}</div>
          <p class="text-gray-500">{{ note.content }}</p>

          <div>
            <button @click="upVoteHandler(note.id)"
                    class="bg-pink-500 text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
            > Like
              <i class="fas fa-heart">{{ note.up_vote }}</i>
            </button>
            <button @click="downVoteHandler(note.id)"
                    class="text-pink-500 bg-transparent border border-solid border-pink-500 hover:bg-pink-500 hover:text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
            >Diss
              <i class="fas fa-heart">{{ note.down_vote }}</i>
            </button>
          </div>
        </div>
        <br>
      </li>

      <!--      <li>-->
      <!--        <br>-->
      <!--        <div class="p-7 max-w-lg mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4">-->
      <!--          <div class="text-xl font-medium text-black">AkiyamaKunka</div>-->
      <!--          <p class="text-gray-500">When will cat become a cat girl at night?</p>-->

      <!--          <div>-->
      <!--            <button-->
      <!--                class="bg-pink-500 text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"-->
      <!--                type="button"-->
      <!--            > Like-->
      <!--              <i class="fas fa-heart">1</i>-->
      <!--            </button>-->
      <!--            <button class="text-pink-500 bg-transparent border border-solid border-pink-500 hover:bg-pink-500 hover:text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button"-->
      <!--            >Diss-->
      <!--              <i class="fas fa-heart">2</i>-->
      <!--            </button>-->
      <!--          </div>-->

      <!--        </div>-->
      <!--        <br>-->
      <!--      </li>-->
      <!--      <li>-->
      <!--        <br>-->
      <!--        <div class="p-7 max-w-lg mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4">-->
      <!--          <div class="text-xl font-medium text-black">Senior ZJY</div>-->
      <!--          <p class="text-gray-500">I love the cookies of ByteDance... Yummy...</p>-->

      <!--          <div>-->
      <!--            <button-->
      <!--                class="bg-pink-500 text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"-->
      <!--                type="button"-->
      <!--            > Like-->
      <!--              <i class="fas fa-heart">2</i>-->
      <!--            </button>-->
      <!--            <button class="text-pink-500 bg-transparent border border-solid border-pink-500 hover:bg-pink-500 hover:text-white active:bg-pink-600 font-bold uppercase text-xs px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button"-->
      <!--            >Diss-->
      <!--              <i class="fas fa-heart">2</i>-->
      <!--            </button>-->
      <!--          </div>-->

      <!--        </div>-->
      <!--        <br>-->
      <!--      </li>-->
    </ul>
    <br>


    <div class="relative flex w-full flex-wrap items-stretch mb-3" style="width:500px; margin: auto" v-if="is_login">
      <input v-model="content" type="text" placeholder="Leave your comment here!"
             class="px-3 py-4 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-base border-0 shadow outline-none focus:outline-none focus:ring w-full pr-10"/>
      <span
          class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-lg items-center justify-center w-8 right-0 pr-3 py-4">
    <i class="fas fa-user"></i>
  </span>
      <button @click="submitNoteHandler"
              style="width: 500px; margin: auto"
              class="bg-pink-400 hover:bg-pink-500 text-white font-bold py-3 px-5 border-b-4 border-pink-600 hover:border-pink-500 rounded">
        Leave a comment.

      </button>
    </div>


    <br>
    <br><br>


    <!--    <ul>-->
    <!--      <li v-for="(note, index) in notes" :key="index">-->
    <!--        <p>-->
    <!--          Post: {{ note.content }}-->
    <!--        </p>-->
    <!--        <p>-->
    <!--          upvote: {{ note.upvote }}-->
    <!--        </p>-->
    <!--        <p>-->
    <!--          downvote: {{ note.downvote }}-->
    <!--        </p>-->
    <!--      </li>-->
    <!--    </ul>-->


    <div class="w-full max-w-lg" style="margin: auto" v-if="!is_login">
      <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input v-model="username"
                 class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                 id="username" type="text" placeholder="Username">
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input v-model="password"
                 class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                 id="password" type="password" placeholder="******">
          <p class="text-red-300 text-xs italic">Please choose a password.</p>
        </div>
        <div class="flex items-center justify-between">
          <button
              class="bg-pink-500 hover:bg-pink-700 text-white font-bold py-2 px-9 rounded focus:outline-none focus:shadow-outline"
              type="button">
            <span v-if='!is_login' @click="loginHandler">Login</span>
          </button>
          <button
              class="bg-pink-500 hover:bg-pink-700 text-white font-bold py-2 px-9 rounded focus:outline-none focus:shadow-outline"
              type="button" @click="signInHandler">
            <span v-if='!is_login'>Sign In</span>
          </button>

          <a class="inline-block align-baseline font-bold text-sm text-pink-500 hover:text-pink-800" href="#">
            Forgot Password?
          </a>
        </div>
      </form>


    </div>
    <p class="text-center text-gray-500 text-xs">
      &copy;2021 AkiyamaKunka. All rights reserved.
    </p>

    <!--    <div id="nav">-->
    <!--      <router-link to="/">Home</router-link> |-->
    <!--      <router-link to="/about">About</router-link>-->
    <!--    </div>-->
    <!--    <router-view/>-->
  </div>
</template>


<script>
export default {
  name: 'App',
  props: {},
  data() {
    return {
      notes: [],
      is_login: false,
      username: 'AkiyamaKunka',
      password: '',
      user_id: '',
      content: '',
    }
  },
  mounted() {
    this.$http.get('guestbook/note-create/')
        .then((response) => {
          this.notes = response.data
          console.log(this.notes)
        })
  },
  methods: {
    loginHandler: function () {
      this.$http.post('login/', {
        username: this.username,
        password: this.password
      }).then((response) => {
        alert('Login successful')
        console.log(response)
        const data = response.data
        localStorage.token = data.token
        localStorage.user_id = data.id
        localStorage.username = data.username

        this.is_login = true;
        // this.$router.push({ name: 'Home', params: { name: this.Username } })
      }).catch(function (error) {
        console.log(error)
        alert('Please check your username and password.')
      })
    },
    signInHandler: function () {
      this.$http.post('guestbook/user-create/user_create_handler/', {
        username: this.username,
        password: this.password
      }).then((response) => {
        console.log(response)
        alert('You have successfully regisetered your account!')
      }).catch((error) => {
        console.log(error)
        alert('Registration failed.')
      })
    },
    submitNoteHandler() {
      this.$http.post('guestbook/note-create/', {
            username: this.username,
            content: this.content,
            up_vote: 0,
            down_vote: 0
          }
      ).then((response) => {
        console.log(response)
      })
    },

    upVoteHandler(note_id) {
      if (this.is_login) {
        this.$http.post('guestbook/note-update/up_vote/', { // 这里地址依然不对
          user_id: localStorage.user_id,
          note_id: note_id,
          // username: this.username,
          // content: this.content
        }).then((response) => {
          alert("thumbs down!")
          console.log(response)
        })
      }
    },
    downVoteHandler(note_id) {
      if (this.is_login) {
        this.$http.post('guestbook/note-update/down_vote/', { // 这里地址依然不对
          user_id: localStorage.user_id,
          note_id: note_id,
          // username: this.username,
          // content: this.content
        }).then((response) => {
          alert("thumbs down!")
          console.log(response)
        })
      }
    },


  },

}


</script>

<style>

html {
  background-color: #eee;
}

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

