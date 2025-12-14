<template>
  <div class="admin-layout">
    <index-header></index-header>
    <index-aside></index-aside>
    <index-main></index-main>
  </div>
</template>

<script>
import IndexHeader from '@/components/index/IndexHeader'
import IndexAside from '@/components/index/IndexAsideStatic'
import IndexMain from '@/components/index/IndexMain'

export default {
  name: 'AdminLayout',
  components: {
    IndexHeader,
    IndexAside,
    IndexMain
  }
}
</script>

<style lang="scss" scoped>
.admin-layout {
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
</style>
