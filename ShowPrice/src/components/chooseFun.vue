<template>
    <div id="app">
        <el-row>
            <el-col :span="12">
                <router-link :to="{ name: 'article', params: { id: item.No }}">
                京东代码
                </router-link>
            </el-col>
            <el-col :span="12">
                
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {};
</script>
<style>

</style>

