<template>
  <div class="bg-color-brown">
    <notifications position="top center" ignoreDuplicates width=400 height=700 group="foo" />
    <Header :brands="brands"></Header>
    <BannerTop />
    <div class="section section-info-customer pd-top-20">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-11 col-12 no-pd">
            
            <h5>Thông tin tài khoản</h5>
          </div>
        </div>
        <div class="row justify-content-center">
          <div
            class="
              col-md-6 col-12
              bg-white
              bd-rd-5
              mg-bottom-20
              table-responsive
            "
          >
            <span
              style="
                font-size: 18px;
                margin-top: 10px;
                display: block;
                color: #5d5d5d;
              "
              >Thông tin cá nhân</span
            >
            <table class="table table-borderless align-middle">
              <input type="hidden" name="user_id" value="' . $id . '" />
              <tbody>
                <tr>
                  <td>Avatar</td>
                  <td><img :src="preview" width="100px" height="auto" />
                  <input v-if="isediting === true" type="file"  accept="image/png, image/jpeg" @change="onFileChange" /></td>
                </tr>
                <tr>
                  <td>Firstname</td>
                  <td>
                    <input
                      type="text"
                      v-model="user.first_name"
                      :disabled="!isediting"
                      class="form-control"
                    />
                  </td>
                </tr>
                <tr>
                  <td>Lastname</td>
                  <td>
                    <input
                      type="text"
                      v-model="user.last_name"
                      :disabled="!isediting"
                      class="form-control"
                    />
                  </td>
                </tr>
                <tr>
                  <td>Email</td>
                  <td>
                    <input
                      class="form-control"
                      type="email" v-model="user.email" :disabled="!isediting"
                    />
                  </td>
                </tr>
                                <tr>
                  <td>Phone</td>
                  <td>
                    <input
                      class="form-control"
                      type="email" v-model="user.phonenum" :disabled="!isediting"
                    />
                  </td>
                </tr>
                <tr>
                  <td></td>
                  <td>
                    <input
                      v-if="isediting === false"
                      type="button"
                      @click="usereditinfo('useremail')"
                      class="btn btn-danger"
                      value="Chỉnh sửa"
                    />
                    <button class="btn btn-danger" v-else type="button" @click="submituser()">Lưu thay đổi</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="col-md-5 col-12 mg-left-20 bg-white bd-rd-5 mg-bottom-20">
            <span
              style="
                font-size: 18px;
                margin-top: 10px;
                display: block;
                color: #5d5d5d;
              "
              >Thông tin đăng nhập</span
            >

            <table class="table table-borderless align-middle">
              <tr>
                <td>Tài khoản</td>
                <td>
                  <input
                    type="text"
                    readonly="readonly"
                    class="form-control"
                    :value="$auth.user.username"
                    disabled
                  />
                </td>
              </tr>
              <tr>
                <td>Password</td>
                <td>
                  <input v-if="!isediting1" type="password" value="********"  class="form-control" disabled  />
                  <input v-else type="password" v-model="password" class="form-control" />
                </td>
              </tr>
              <tr v-if="isediting1">
                <td>New password</td>
                <td>
                  <input type="password" v-model="new_password" class="form-control" />
                </td>
              </tr>
              <tr v-if="isediting1">
                <td>Retype password</td>
                <td>
                  <input type="password" v-model="rnew_password" class="form-control" />
                </td>
              </tr>
              <tr v-if="status != ''">
                <td>

                </td>
                <td class="bg-danger">
                  {{ status }}
                </td>
              </tr>
              <tr>
                <td></td>
                <td>
                  <input
                      v-if="isediting1 === false"
                      type="button"
                      @click="usereditpassword('')"
                      class="btn btn-danger"
                      value="Chỉnh sửa"
                    />
                  <input
                    v-else
                    type="button"
                    class="btn btn-danger"
                    value="Lưu thay đổi"
                    @click="changepassword "
                  />
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>
    <Top-footer />
    <Footer />

  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    let user = await $axios.$get('/user/')
    user = user.user
    const preview = user.img
    const brands = await $axios.$get('/brand/')
    return { user, preview, brands }
  },
  data() {
    return {
      user: {
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        phonenum:'',
        img: '',
      },
      password: '',
      new_password: '',
      rnew_password: '',
      preview: '',
      status: '',
      isediting: false,
      isediting1: false,
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.user.img = files[0]
      this.createImage(files[0])
    },
    createImage(file) {
      const reader = new FileReader()
      const vm = this
      reader.onload = (e) => {
        vm.preview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    usereditinfo() {
      this.isediting = !this.isediting
    },
    usereditpassword() {
      this.isediting1 = !this.isediting1
    },
    async submituser() {
      const config = {
        headers: { 'content-type': 'multipart/form-data' },
      }
      const formData = new FormData()
      for (const data in this.user) {
        formData.append(data, this.user[data])
      }
      try {
        const respons= await this.$axios.post('/updateuser/', formData, config)
        this.usereditinfo()
        console.log(respons)
        if (respons.status ===202){
          this.$notify({
            group: 'foo',
            title: 'Notification',
            text: "Change user informations successfuly",
          })
        }
        
      } catch (e) {
        if(e.response.status ===409){
          this.status="This Email already used!"
        }
        this.$notify({
            group: 'foo',
            type:'error',
            title: 'Error',
            text: this.status,
          })
      }
      
      await this.$auth.fetchUser()
    },
    async changepassword() {
      const config = {
        headers: { 'content-type': 'multipart/form-data' },
      }
      const formData = new FormData()
      formData.append('password', this.password)
      formData.append('new_password', this.new_password)
      formData.append('rnew_password', this.rnew_password)
      try{
        const response = await this.$axios.post('/changepass/', formData, config)
        if(response.status===202){
          this.status="Password change successfuly!"     // add nofi
          this.$notify({
            group: 'foo',
            title: 'Notification',
            text: this.status,
          })
        }
      }
      catch (e) {
        if(e.response.status===400){
          this.status="Incorrect Password"  
          
        }
        else if (e.response.status ===412){
          this.status="Password not strong enough!"  
        }
        else{
          this.status="New password does't match!"
        }
        this.$notify({
            group: 'foo',
            type:'error',
            title: 'Error',
            text: this.status,
          })
      }
      this.$nuxt.refresh()
    },
  },
}
</script>
