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
            <b-nav-item-dropdown text="Texte">
              <b-dropdown-item href="#" class="dropdown-mine" variant="success"
                ><b-nav-item to="/maptext" class="dark"
                  >Carte avec lieux</b-nav-item
                ></b-dropdown-item
              >
              <b-dropdown-item href="#" class="dropdown-mine"
                ><b-nav-item to="/itinerarytext" class="dark"
                  >Itinéraire</b-nav-item
                ></b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown text="Lieux">
              <b-dropdown-item href="#" class="dropdown-mine" variant="success"
                ><b-nav-item to="/maplocations" class="dark"
                  >Carte avec lieux</b-nav-item
                ></b-dropdown-item
              >
              <b-dropdown-item href="#" class="dropdown-mine"
                ><b-nav-item to="/itinerarylocations" class="dark"
                  >Itinéraire</b-nav-item
                ></b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item to="/upload">Importer</b-nav-item>
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
  align-items: left;
  flex-direction: column;
  text-align: center;
  color: #fff;
  font-size: 1.6rem;
}

.dark .nav-link {
  color: #009879 !important;
}

</style>
