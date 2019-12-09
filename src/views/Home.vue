<template>
    <div class="chartBox">
        <el-form :inline="true" :model="formInline" class="" size="small" ref="myform">
            <el-form-item  prop="platform">
                <el-select v-model="formInline.platform" placeholder="平台"  value="">
                    <el-option label="全部" value="all"></el-option>
                    <el-option label="金业" value="pm"></el-option>
                    <el-option label="钜丰" value="jf"></el-option>
                    <el-option label="投资" value="lh"></el-option>
                    <el-option label="微投" value="wt"></el-option>
                    <el-option label="智投" value="zt"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item  prop="faultLevel">
                <el-select placeholder="故障等级" v-model="formInline.faultLevel" value="" @change="formItemChange('faultType',1)">
                    <el-option label="全部" value="all"></el-option>
                    <el-option label="P0" value="P0"></el-option>
                    <el-option label="P1" value="P1"></el-option>
                    <el-option label="P2" value="P2"></el-option>
                    <el-option label="P3" value="P3"></el-option>
                    <el-option label="P4" value="P4"></el-option>
                    <el-option label="P5" value="P5"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item  prop="faultType">
                <el-select v-model="formInline.faultType" placeholder="故障类型" value=""  @change="formItemChange('faultLevel',1)">
                    <el-option label="全部" value="all"></el-option>
                    <el-option label="网络问题" value="net"></el-option>
                    <el-option label="app问题" value="app"></el-option>
                    <el-option label="人为原因" value="personal"></el-option>
                    <el-option label="程序原因" value="bug"></el-option>
                    <el-option label="客户原因" value="client"></el-option>
                    <el-option label="新的需求" value="command"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item prop="dateType" required>
                <el-select v-model="formInline.dateType" placeholder="时间类型" value=""  >
                    <el-option label="天" value="day"></el-option>
                    <el-option label="周" value="week"></el-option>
                    <el-option label="月" value="month"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item prop="daterange" v-show="formInline.dateType==='day'">
                <el-date-picker type="daterange"
                                value-format="yyyy-MM-dd"
                                align="center"
                                range-separator="至"
                                start-placeholder="开始日期"
                                clearable
                                end-placeholder="结束日期"
                                v-model="formInline.daterange">
                </el-date-picker>
            </el-form-item>
            <el-form-item prop="monthrange" v-show="formInline.dateType==='month'">
                <el-date-picker type="monthrange"
                                value-format="yyyy-MM"
                                align="left"
                                range-separator="至"
                                start-placeholder="开始月份"
                                clearable
                                end-placeholder="结束月份"
                                v-model="formInline.monthrange">
                </el-date-picker>
            </el-form-item>
            <el-form-item prop="weekrange" v-show="formInline.dateType==='week'" required>
                <el-date-picker type="week"
                                format="yyyy 第 WW 周"
                                align="left"
                                placeholder="开始周"
                                clearable

                                v-model="formInline.weekrange[0]">
                </el-date-picker>
                至
                <el-date-picker type="week"
                                align="center"
                                format="yyyy 第 WW 周"
                                placeholder="结束周"
                                clearable
                                required
                                v-model="formInline.weekrange[1]">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">查询</el-button>
            </el-form-item>
            <el-form-item>
                <el-button type="default" @click="onReset">重置</el-button>
            </el-form-item>
        </el-form>
        <div class="eachChart">
            <ve-line :data="chartData" :loading="loading" :title="title" :toolbox="toolbox" :legend="legend"></ve-line>
        </div>
    </div>
</template>
<script>
    import moment from 'moment'
    import axios from 'axios'
    import 'echarts/lib/component/toolbox'
    import 'echarts/lib/component/title'
    import 'echarts/lib/component/legend'
    import 'echarts/lib/component/legendScroll'
    import 'v-charts/lib/style.css'
    export default {
        name: "chart",
        data() {
            return {
                formInline: {
                    platform: 'all',
                    faultLevel: '',
                    faultType: '',
                    dateType:'week',
                    daterange: '',
                    weekrange:[],
                    monthrange:''
                },
                loading:false,
                toolbox: {
                    feature: {
                        magicType: {type: ['line', 'bar', 'pie']},
                        saveAsImage: {},
                    },
                    right:'15%'
                },
                chartData: {
                    columns: [],
                    rows:[],
                },
                title:{
                    text:'所有平台的故障总数统计',
                    textAlign:'center',
                    left:'50%',
                },
                legend:{
                    type: 'scroll',
                    orient: 'vertical',
                    right: 10,
                    // top: 20,
                    // bottom: 20,
                },
                piedata: {
                    columns: ['platform', 'number'],
                    rows: [
                        {'platform': 'PM', 'number': 1393},
                        {'platform': 'LH', 'number': 3530},
                        {'platform': 'JF', 'number': 2923},
                        {'platform': 'WT', 'number': 1723},
                        {'platform': 'ZT', 'number': 3792},
                    ]

                }
            }
        },
        methods: {
            onSubmit() {
                let reqdata = {}
                reqdata.dateType  = this.formInline.dateType
                reqdata.platform  = this.formInline.platform
                reqdata.faultLevel  = this.formInline.faultLevel
                reqdata.faultType  = this.formInline.faultType
                // if(this.formInline.dateType==='week'){
                //     weekRange.push(moment(this.formInline.weekrange[0]).format('YYYY-WW'))
                //     weekRange.push(moment(this.formInline.weekrange[1]).format('YYYY-WW'))
                //     reqdata.weekrange = weekRange
                // }
                switch(this.formInline.dateType){
                    case "week":
                        var weekRange = []
                        weekRange.push(moment(this.formInline.weekrange[0]).format('YYYY-WW'))
                        weekRange.push(moment(this.formInline.weekrange[1]).format('YYYY-WW'))
                        reqdata.weekrange = weekRange
                        break;
                    case 'month':
                        reqdata.monthrange = this.formInline.monthrange
                        break
                    case 'day':
                        reqdata.monthrange = this.formInline.daterange
                }
                window.console.log(reqdata)
               this.getdata()
                let platform = 'quanbu'
                let fault_level = '54353'
                this.title.text = `${platform}平台${fault_level}故障统计`
            },
            onReset() {
                this.$refs['myform'].resetFields();
            },
            formItemChange(value, number) {
                if (this.formInline[value] !== '') {
                    if (number === 1) {
                        this.$message({
                            type:'warning',
                            message:'故障级别和故障类型只能选择其中一个',
                            showClose:true,
                            duration:2000
                        })
                    }
                    if (number === 2) {
                        // this.$message.warning('日期和日期范围只能选择其中一个')
                        return
                    }
                    this.formInline[value] = ''
                }
            },
            getdata() {
                this.loading=true
                setTimeout(()=>{
                    axios.get('http://127.0.0.1:5000/getdata').then(res => {
                        this.chartData = res.data.data
                        // this.chartData.columns = res.data.columns
                        // this.chartData.rows = res.data.rows
                        this.loading=false
                    }).catch(error => window.console.log(error))
                },1000)
            },
        },
        created() {
            this.getdata()
        }
    }
</script>
<style>
    .chartBox{
        width: 100%;
        padding: 20px;
    }
    .eachChart{
        display: inline-block;
        width:50%;
        padding-top: 50px;
    }
</style>