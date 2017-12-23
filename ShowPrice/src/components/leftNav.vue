<template>
    <div id="app">
        <el-row class="tac">
            <el-col>
                <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" router="true">
                    <el-submenu index="1">
                        <template slot="title">
                            <i class="el-icon-location"></i>
                            <span>爬虫</span>
                        </template>
                        <el-menu-item-group>
                            <template slot="title">苏州公交</template>
                            <el-menu-item index="/busShow">增加数据</el-menu-item>
                            <el-menu-item index="/busShow">查询数据</el-menu-item>
                        </el-menu-item-group>
                        <el-menu-item-group title="分组2">
                            <el-menu-item index="1-3">选项3</el-menu-item>
                        </el-menu-item-group>
                        <el-submenu index="1-4">
                            <template slot="title">选项4</template>
                            <el-menu-item index="1-4-1">选项1</el-menu-item>
                        </el-submenu>
                    </el-submenu>
                    <el-menu-item index="2">
                        <i class="el-icon-menu"></i>
                        <span slot="title">导航二</span>
                    </el-menu-item>
                    <el-menu-item index="3">
                        <i class="el-icon-setting"></i>
                        <span slot="title">导航三</span>
                    </el-menu-item>
                </el-menu>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {};
</script>
<style>

</style>