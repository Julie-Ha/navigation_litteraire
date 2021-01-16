<template>
  <div id="navbar">
    <b-navbar
      toggleable="lg"
      type="dark"
      style="background-color: #009879;"
      fixed="top"
    >
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <div class="menu">
          <b-navbar-nav>
            <b-nav-item to="/">Texte</b-nav-item>
            <b-nav-item to="/locations">Lieux</b-nav-item>
            <b-nav-item to="/itinerary">Itinéraires</b-nav-item>
            <b-nav-item to="/upload">upload</b-nav-item>
          </b-navbar-nav>
        </div>
      </b-collapse>
    </b-navbar>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>
<style lang="scss">
.fix-top {
  margin-top: -63px;
}
.menu {
  width: 100%;
  bottom: 0;
  display: flex;
  align-items: center;
  flex-direction: column;
  text-align: center;
  color: #fff;
  font-size: 1.6rem;
}

.dark .nav-link {
   color: #009879 !important;
}
</style>
