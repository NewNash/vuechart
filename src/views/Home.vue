<template>
    <div>
        <el-form :inline="true" :model="formInline" class="" size="small" ref="myform">
            <el-form-item  prop="platform">
                <el-select v-model="formInline.platform" placeholder="平台" clearable value="">
                    <el-option label="全部" value="all"></el-option>
                    <el-option label="金业" value="pm"></el-option>
                    <el-option label="钜丰" value="jf"></el-option>
                    <el-option label="投资" value="lh"></el-option>
                    <el-option label="微投" value="wt"></el-option>
                    <el-option label="智投" value="zt"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item  prop="level">
                <el-select placeholder="故障等级" clearable v-model="formInline.level" value="" @change="formItemChange('type',1)">
                    <el-option label="全部" value="all"></el-option>
                    <el-option label="P0" value="P0"></el-option>
                    <el-option label="P1" value="P1"></el-option>
                    <el-option label="P2" value="P2"></el-option>
                    <el-option label="P3" value="P3"></el-option>
                    <el-option label="P4" value="P4"></el-option>
                    <el-option label="P5" value="P5"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item  prop="type">
                <el-select v-model="formInline.type" placeholder="故障类型" value="" clearable @change="formItemChange('level',1)">
                     <el-option label="全部" value="all"></el-option>
                    <el-option label="网络问题" value="net"></el-option>
                    <el-option label="app问题" value="app"></el-option>
                    <el-option label="人为原因" value="personal"></el-option>
                    <el-option label="程序原因" value="bug"></el-option>
                    <el-option label="客户原因" value="client"></el-option>
                    <el-option label="新的需求" value="command"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item  prop="date">
                <el-date-picker type="date" v-model="formInline.date" placeholder="选择日期"
                                @change="formItemChange('daterange',2)">
                </el-date-picker>
            </el-form-item>
            <el-form-item prop="daterange">
                <el-date-picker type="daterange"
                                range-separator="至"
                                start-placeholder="开始日期"
                                end-placeholder="结束日期"
                                @change="formItemChange('date',2)"
                                v-model="formInline.daterange">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">查询</el-button>
            </el-form-item>
            <el-form-item>
                <el-button type="default" @click="onReset">重置</el-button>
            </el-form-item>
        </el-form>

        <ChartBox/>
    </div>
</template>
<script>
    import ChartBox from '@/components/chart.vue'

    export default {
        data() {
            return {
                formInline: {
                    user: '',
                    platform: '',
                    level: '',
                    type: '',
                    date: '',
                    daterange: '',
                },
                count: this.$store.state.count
            }
        },
        components: {
            ChartBox,
        },
        methods: {
            onSubmit() {

            },
            onReset() {
                this.$refs['myform'].resetFields();
            },
            formItemChange(value, number) {
                if (this.formInline[value] !== '') {
                    if (number === 1) {
                        this.$message.warning('故障级别和故障类型只能选择其中一个')
                    }
                    if (number === 2) {
                        this.$message.warning('日期和日期范围只能选择其中一个')
                    }
                    this.formInline[value] = ''
                }
            },
        },
    }
</script>