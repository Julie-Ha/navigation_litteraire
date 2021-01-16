<template>
  <div>
    <b-container style="padding-top:25px">
    <!-- Styled -->
    <div class="row">
        <b-form-file
        v-model="file1"
        :state="Boolean(file1)"
        accept=".pdf, .txt,"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
        >
    
      </b-form-file>
      </div>
      <div class="row pagination">
      <b-button variant="success" v-on:click="submitFile()" >Submit</b-button>
    </div>
</b-container>
          <b-container>
            <div class="row">
              
               <div class="col-12 ">
                  <div class="table-responsive">
                     <table class="content-table table tablesorter">
                        <thead>
                           <tr class="text-center" >
                              <th>N°</th>
                              <th>Fichiers </th>
                              <th>Action </th>
                           </tr>
                        </thead>
                        <tbody>
                           <tr v-for=" (gars,index) in pageOfItems " :key="index.text" class="active-row text-center"  >
                              <td >{{ index +1 }}</td>
                              <td >{{ gars.text}}</td>
                              <td ><b-icon icon="x-circle" scale="2" variant="danger" v-on:click="deletefile(gars.value)"> </b-icon> </td>
                           </tr>
                        </tbody>
                     </table>
                     <div  class="pagination">
                        <jw-pagination :items="locations"  @changePage="onChangePage" ></jw-pagination>
                     </div>
                  </div>
               </div>
            </div>
         </b-container>

  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "Upload_file",

  data() {
    return {
      loading: false,
          file1: null,
        file2: null,
        isDragging: false,
        dragCount: 0,
        files: [],
        selected: 'radio1',
        locations:[] ,
        pageOfItems: [],
    };
  },
  async created() {
    this.loading = true;
    this.liste()
  },
methods: {
    async  submitFile(){
        this.file1;
        let formData = new FormData();
        formData.append('file', this.file1);

        await axios
            .post(
            "http://127.0.0.1:5000/uploader", formData,{headers: {'Content-Type': 'multipart/form-data'}})
            .then((response) => {
            console.log(response.data)
            });
         this.locations = [];

      await axios
        .get(
          "http://127.0.0.1:5000/getList")
        .then((response) => {
          this.locations = response.data
        });
        console.log(this.locations)

      this.loading = true;
       this.file1= null
    
    },
  async  liste(){
    
    console.log(this.$fichier)
    
    this.locations = [];

      await axios
        .get(
          "http://127.0.0.1:5000/getList")
        .then((response) => {
          this.locations = response.data
        });
        console.log(this.locations)

      this.loading = true;
    },
    handleFilesUpload(){
    this.files = this.$refs.files.files;
    },
     onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        },
    async deletefile(locat){
        
        if(locat != null){
            await axios.get(
                "http://127.0.0.1:5000/delete?filles=" +locat)
        .then((response) => {
            console.log(response.data);
            this.liste()
        });
       

        }
      this.loading = true;
    
    }

}

};
</script>
<style lang="scss" scoped>
* {
  font-family: sans-serif; /* Change your font family */
}
.content-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  min-width: 400px;
  border-radius: 5px 5px 0 0;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.content-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
  font-weight: bold;
}
.content-table th,
.content-table td {
  padding: 12px 15px;
}
.content-table tbody tr {
  border-bottom: 1px solid #dddddd;
}
.content-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}
.content-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}
.content-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
.pagination {
           justify-content: center;
           flex-wrap: wrap;
           padding: 10PX;
}
</style>
