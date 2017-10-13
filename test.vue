<style lang="less" scoped>

    @import "../../assets/css/base.less";
    @import '../../assets/css/suggestions/dealerOrders.less';
</style>

<style lang="less">
    .my-dealer-orders {
        overflow: hidden;
        .engineer-list {
            width: calc(~"100% - 90px");
            font-size: 14px;
            color: #999;
            .vux-tap-active {
                width: 100%;
            }
        }
        .item {
            .engineer-note {
                width: calc(~"100% - 90px");

                padding-left: 2px;
                font-size: 14px;
                color: #999;
            }
            .icon-arrow-bottom {
                color: #999;
            }
            &.selected {
                .engineer-list {
                    color: #000 !important;
                }
                .vux-popup-picker-value {
                    color: #000 !important;
                }
                .icon-arrow-bottom {
                    color: #000 !important;
                }
            }
            select {
                width: calc(~"100% - 90px");
                padding: 14px 15px 14px 12px;
            }
        }
    }
    .water-leasing {
        .item {
            select {
                padding-left: 0;
            }
        }
    }
    .vux-popup-picker-select{
        top: 0 !important;
    }



</style>
<template>
    <div>
        <header class="header">
            <i class="icon icon-arrow-left button" @click="clearServiceTime"></i>
            <h2 class="title">租赁净水</h2>
        </header>
        <div class="has-header my-dealer-orders water-leasing">
            <!--经销商信息-->
            <form>
                <label class="item top">
                    <span>经销商编码<sup>*</sup></span>
                    <input type="search"
                           placeholder="请输入"
                           v-model="dealerCode"
                           @change="queryDealerList"
                           @keypress.13="queryDealerList">
                </label>
                <label class="item">
                    <span>经销商名称</span>
                    <input type="text"
                           placeholder="自动带出"
                           v-model="dealerName"
                           readonly>
                </label>
                <label class="item">
                    <span>网点编号</span>
                    <input type="text"
                           placeholder="自动带出"
                           v-model="netWorkCode"
                           readonly>
                </label>
                <label class="item">
                    <span>网点名称</span>
                    <input type="text"
                           placeholder="自动带出"
                           v-model="netWorkName"
                           readonly>
                </label>
            </form>
            <!--用户信息-->
            <label class="item top">
                <span>产品类型</span>
                <div class="fixed-field">{{productName}}</div>
                <!--showXNumber 是为了让这个组件在具体的值赋好之后再加载 避免value赋了初始值-->
                <x-number width="50px"
                          :min="1" :max="99"
                          class="number"
                          v-if="showXNumber"
                          v-model="productNumber"></x-number>
            </label>
            <label class="item"
                   :class="{'selected': selected(serviceRequest[0])}">
                <span>服务请求<sup>*</sup></span>
                <popup-picker
                    head="服务请求"
                    :data="serviceRequestList"
                    v-model="serviceRequest"
                    ref="serviceRequest"></popup-picker>
                <i class="icon icon-arrow-bottom" @click="openRequestPicker"></i>
            </label>

            <label class="item"
                   :class="{'selected': selected(fault[0])}"
                   v-show="isRepair">
                <span>故障类型<sup>*</sup></span>
                <popup-picker :data="faultList" v-model="fault" ref="faultPicker"></popup-picker>
                <i class="icon icon-arrow-bottom" @click="openFaultPicker"></i>
            </label>

            <!--<label class="item"-->
                   <!--:class="{'selected': selected(fault[0])}"-->
                   <!--v-show="isTHJ">-->
                <!--<span>请求类别<sup>*</sup></span>-->
                <!--<popup-picker :data="faultList" v-model=="fault" ref="faultPicke"></popup-picker>-->
                <!--<i class="icon icon-arrow-bottom" @click="openFaultPicker"></i>-->
            <!--</label>-->
            <!-- 验证手机号 -->
            <div class="validate" v-if="isFirstBuy">
                <div>验证手机号码<sup>*</sup></div>
                <div class="phone-item">
                    <label>
                        <input type="tel"
                               pattern="[0-9.]*"
                               placeholder="请输入您的手机号"
                               v-model="userPhone">
                    </label>
                    <div class="code"
                         v-if="imsTxt === '发送验证码'"
                         @click.stop.prevent="sendCode">发送验证码</div>
                    <div class="code" v-else>{{imsTxt}}</div>
                </div>
                <label class="sms">
                    <input type="tel" placeholder="请输入短信中的验证码" v-model="imsCode">
                </label>
            </div>
            <label class="item top">
                <span>用户名称<sup>*</sup></span>
                <input type="text" placeholder="请输入" v-model="userName">
            </label>
            <label class="item">
                <span>用户电话<sup>*</sup></span>
                <input type="tel" placeholder="请输入" v-model="userMobile" @blur="validateMobile">
            </label>
            <label class="item">
                <span>客户公司<sup>*</sup></span>
                <input type="text" placeholder="请输入" v-model="customerCompany">
            </label>
            <label class="area-item">
                <span>所在区域<sup>*</sup></span>
                <router-link class="select-div"
                             :class="[selectArea ? 'is-select': '']"
                             to="/selectProvince">
                    <div class="area-div">{{selectArea ? selectArea : '请选择所在区域'}}</div>
                    <div class="icon-arrow-right"></div>
                </router-link>

            </label>
            <label class="item">
                <span>详细地址<sup>*</sup></span>
                <input type="text" placeholder="请输入" v-model="address">
            </label>
            <label class="item">
                <span>预约时间<sup>*</sup></span>
                <router-link class="select-div"
                             :class="[serviceTime.time ? 'is-select': '']"
                             to="/serviceTime">
                    <div class="area-div">{{ serviceTime.date ? serviceTime.date + ' ' + serviceTime.time : '请选择预约的服务时间' }}</div>
                    <div class="icon-arrow-right"></div>
                </router-link>
            </label>
            <!-- 问题描述 -->
            <label class="textarea-div top">
                <x-textarea class="area-content"
                            :max="90"
                            :placeholder="questionTypeContent"
                            :rows="3"
                            v-model="memo">
                </x-textarea>
            </label>
            <!-- 底部提交按钮 -->
            <div class="footer" @click.stop.prevent="checkData">
                <div>提交</div>
            </div>
        </div>
        <loading v-model="loadingShow" :text="loadingTxt"></loading>
        <!--<loading2 :show="loadingShow2"></loading2>-->
        <Jump v-model="jumpAlertShow" :button-text.sync="alertButton" title="" @on-hide="goProgress">{{ jumpAlertTxt }}</Jump>
        <alert v-model="alertShow" :button-text.sync="alertButton" title="">{{ alertTxt }}</alert>
    </div>

</template>

<script>
import {Alert,Loading ,Badge,PopupPicker,XTextarea,XNumber} from 'vux'
export default {
    components: {
        Jump: Alert,
        Alert,
        Loading ,
        Badge,
        PopupPicker,
        XTextarea,
        XNumber
    },
    computed: {
        isRepair: function() {
            return this.serviceRequest[0] === '维修';
        },
        isTHJ: function () {
            return this.serviceRequest[0] === '退机' || this.serviceRequest[0] === '换机';
        }
    },
    watch: {
        'isRepair': function (newValue) {
            if(newValue) {

                this.getFaultAtion('BX');
            }
        },
        'isTHJ': function (newValue) {
            if (newValue) {
                this.getFaultAtion('TH');
            }
        }
    },

    mounted() {

        // 获取缓存内容
        const serviceTimeStr = this.store('shopping').serviceTime,
            addressItemStr = this.store('address').addressItem,
            dealerCode = this.store('suggestions').dealerCode,
            pageCacheStr = this.store('suggestions').pageCache,
            pageCache = pageCacheStr ? JSON.parse(pageCacheStr) : {};
        console.log(pageCache)

        // 赋值时间、地址
        this.serviceTime = serviceTimeStr ? JSON.parse(serviceTimeStr) : {};
        this.addressItem = addressItemStr ? addressItemStr : {};

        /**
         * 首次下单校验是否注册
         */
        if (this.bindPhone) {
            this.isFirstBuy = false;
        }

        // 从别的页面选择回来
        if (pageCache.hasOwnProperty('dealerCode')) {
            Object.assign(this.$data, pageCache);
        } else { // 只缓存了经销商编码
            if (dealerCode) {
                this.dealerCode = dealerCode;
                this.queryDealerList();
            }
        }

        // 从别的页面回来 获取具体的产品数量再加载组件
        this.showXNumber = true;

        // 有街道名称就说明拿到四级地址了.
        if (this.addressItem.hasOwnProperty('streetName')) {
            this.selectArea = this.addressItem.provinceName
                + this.addressItem.cityName
                + this.addressItem.countyName
                + this.addressItem.streetName;
        }

        this.hasCommit = false;

//        /**
//         * @desc 离开页面把内容缓存下来
//         **/
//        deactivate: function() {
//            const addressItem = sessionStorage.getItem('addressItem');
//
//            // 只缓存经销商编码 每次进入页面需要重新获取一次经销商信息
//            if (this.dealerCode && this.dealerName && this.netWorkCode && this.netWorkName) {
//                localStorage.setItem('dealerCode', this.dealerCode);
//            }
//
//            // 地址做本地缓存
//            if (addressItem) {
//                localStorage.setItem('addressItem', addressItem);
//            }
//        }
    },
    data() {
        return {

            isFirstBuy: false, // 是否第一次购买
            hasCommit: false, // 是否正在提交
            imsCode: '', // 验证码
            userPhone: '', // 用户电话
            imsTxt: '发送验证码', // 发送验证码后的文字提示
            engineerInfoList: {}, // 放置工程师信息 以{工程师名称：工程师的形式}保存
            engineerList: [
                []
            ],  // 工程师列表
            engineer: ['请选择'], // 工程师的选择value engineer[0]的方式获取
            engineerFlag: false, // 是否打开下拉开关
            engineerPc: '请选择', // PC端工程师默认选择
            engineerNote: '请先输入经销商编码', // 工程师下拉提示
            timeLeave: 60, // 一分钟一次手机验证
            dealerCode: '', // 经销商编码
            dealerName: '', // 经销商名称
            netWorkCode: '', // 网点编号
            netWorkName: '', // 网点名称
            productName: '租赁净水', // 产品名称
            serviceRequest: ['请选择'],
            serviceRequestList: [
                ['请选择', '维修', '安装-自动开机', '安装-手动开机', '用户要求退机', '用户要求换机']
            ],
            productNumber: 1, // 默认数量为1台
            showXNumber: false, // 是否加载x-number组件
            userName: '', // 用户名称
            userMobile: '', // 用户验证手机号
            customerCompany: '', // 客户公司
            selectArea: '', // 所在区域
            address: '', // 详细地址
            memo: '', // 备注信息
            faultMap: {},
            faultList: [ // 故障类型选项列表
                ['请选择故障类型']
            ],
            fault: [ // 故障类型选项值
                '请选择故障类型'
            ],
            faultFlag: false, // 故障类型选项开关
            serviceTime: {}, // 服务时间
            addressItem: {}, // 地址
            questionTypeContent: '备注信息',
            jumpAlertShow: false, // 跳转前弹框
            jumpAlertTxt: '', // 跳转前弹框文字
            loadingQuery: false, // 是否正在请求经销商信息

        }
    },
    beforeRouteLeave: function(to,from,next){
        if (to.path == '/selectProvince' || to.path == '/serviceTime') {
            this.saveTempData();
        }
        next();
    },
    methods: {
        /**
         * 验证手机号
         */
        validateMobile: function () {
            if (!(/^1[3|4|5|7|8][0-9]\d{8}$/.test(this.userMobile))) {
                this.showTips('请输入正确的电话号码格式');
                return;
            }
        },
        /**
         * 是否选择了内容
         */
        selected: function(str) {
            if (!str) return false;
            return str !== '请选择' && str !== '请选择故障类型';
        },
        /**
         * 打开故障类型选择
         */
        openFaultPicker() {
            if(this.faultFlag) {
                this.$refs.faultPicker.onClick();
            }
        },
        /**
         * 打开工程师选择
         */
        openEngineerPicker() {
            if(this.engineerFlag) {
                this.$refs.engineerpop.onClick();
            }
        },
        openRequestPicker() {
            console.log(this.$refs.serviceRequest)
            this.$refs.serviceRequest.onClick();

        },
        /**
         * 根据经销商编码获取经销商信息
         */
        queryDealerList() {
            const params = {
                json:{
                        "headers": {
                            "reqSystemCode": "JSXWX", // 经销商列表查询固定字段
                            "reqTime": new Date().getTime()
                        },
                        "body": {
                            "salesUnitCode": this.dealerCode
                        }
                 }

            };

            this.loadingQuery = true;
            this.showLoading();
            this.api('suggestions').queryStoreUnitList(params).then(succResp => {
                //  请求成功
                if (succResp.status ==true) {
                    // 请求成功 就把工程师列表清掉
                    this.engineerList[0] = ['请选择'];

                    // 本来选择的工程师还原成请选择
                    this.engineerPc = '请选择';
                    this.engineer = ['请选择'];

                    if (succResp.hasOwnProperty('storeUnitVOList')) {
                        // 如果返回的经销商信息长度不大于0
                        if (!(succResp.storeUnitVOList.length > 0)) {
                            this.showTips('亲，查询不到该经销商编码哦！');
                            this.dealerName = '';
                            this.netWorkCode = '';
                            this.netWorkName = '';
                            this.engineerNote = '请输入正确的经销商编码';
                            this.engineerFlag = false;
                        } else {
                            // 有数据默认把第一条的数据显示出来
                            const temp = succResp.storeUnitVOList[0];
                            this.dealerName = temp['salesUnitName'];
                            this.netWorkCode = temp['unitCode'];
                            this.netWorkName = temp['unitName'];

                            // 打开工程师下拉开关
                            this.engineerFlag = true;

                            if(temp['storeUnitEngineerList']) {
                                let engineerList = temp['storeUnitEngineerList'],
                                    len = engineerList.length,
                                    i = 0;
                                for (; i < len; i++) {
                                    this.engineerList[0].push(engineerList[i]['engineerName']);
                                    this.engineerInfoList[engineerList[i]['engineerName']] = engineerList[i];
                                }
                            }
                        }
                        this.closeLoading();
                        this.loadingQuery = false;
                    } else {
                        this.closeLoading();
                        this.showAlert(succResp.data.errorMsg || $conf.msg.errMsg);
                    }
                } else {
                    this.closeLoading();
                    this.showAlert(succResp.data.errorMsg || $conf.msg.errMsg);
                }
            }, () => {
                // 请求失败
                this.closeLoading();
                this.showAlert($conf.msg.errMsg);
            });
        },
        /**
         *  根据产品的 productTypeId 来获取故障类型可选列表
         * @param faultType 故障类型 BX TH
         */
        getFaultAtion(faultType) {


            const params = {
                interfaceSource: 'MMJYWX',
                prodCode: '1123',
                brandCode: 'MIDEA',
                depth: 3,
                parentServiceRequireCode: faultType
            };
            this.api('common').getFault(params).then((succResp) => {
                //  请求成功
                if (succResp.status == true && succResp.content) {
                        this.faultList = [];
                        const result = succResp.content,
                            len = result.length;
                        if (result && len > 0) {
                            let tmpFaultList = []; // 存储过渡的故障

                            tmpFaultList.push('请选择故障类型');

                            let i = 0;
                            for (; i < len; i++) {
                                let tmpData = result[i];

                                tmpFaultList.push(tmpData.faultTypeName);
                                this.faultMap[tmpData.faultTypeName] = tmpData; // 名字与详细的对照关系
                            }
                            this.faultList.push(tmpFaultList);
                            if (this.faultList[0].indexOf(this.fault[0]) < 0) {
                                this.fault = ['请选择故障类型']; // 还原值
                            }
                            this.$nextTick(function() {
                                this.faultFlag = true;
                            });
                    } else {
                        this.showAlert(succResp.data.error.errMsg || $conf.msg.errMsg + '错误信息：移动中控获取故障列表-' + succResp.status);
                    }
                } else {
                    this.showAlert(succResp.data.error.errMsg || $conf.msg.errMsg + '错误信息：移动中控获取故障列表-' + succResp.status);
                }

            }, (res) =>{
                // 请求失败
                this.showAlert($conf.msg.errMsg + '错误信息：移动中控获取故障列表' + res.status);

            });
        },
        /**
         * @name 缓存页面数据
         */
        saveTempData() {
            // 缓存页面数据 比如跳到地址页面选择 或者跳到服务时间选择页面
            const tempData = {
                dealerCode: this.dealerCode,
                dealerName: this.dealerName,
                netWorkCode: this.netWorkCode,
                netWorkName: this.netWorkName,
                engineerInfoList: this.engineerInfoList,
                engineerList: this.engineerList,
                engineer: this.engineer,
                engineerPc: this.engineerPc,
                engineerNote: this.engineerNote,
                engineerFlag: this.engineerFlag,
                serviceRequestList: this.serviceRequestList,
                serviceRequest: this.serviceRequest,
                faultMap: this.faultMap,
                faultList: this.faultList,
                fault: this.fault,
                customerCompany: this.customerCompany,
                userPhone: this.userPhone,
                imsCode: this.imsCode,
                userName: this.userName,
                userMobile: this.userMobile,
                productNumber: this.productNumber,
                address: this.address,
                memo: this.memo
            };

            // 有经销商编码再保存
            if (this.dealerCode) {
                this.store('suggestions').pageCache = JSON.stringify(tempData)
                console.log(this.store('suggestions').pageCache)
            }
        },
        /**
         * 跳转
         */
        goProgress() {
            this.clearData();
            this.jumpAlertShow = false;

            let timeOut = setTimeout(() => {
                this.goPage('progress',{} ,true);
                clearTimeout(timeOut);
            }, 300);
        },
        /**
         * 清除缓存
         */
        clearData() {
            if(this.store('suggestions').pageCache) {
                this.store('suggestions').pageCache = ''
            }
            if(this.store('address').selectArea) {
                this.store('address').selectArea = ''
            }
            if(this.store('address').selectCity) {
                this.store('address').selectCity=''
            }
            if(this.store('address').selectProvince) {
                this.store('address').selectProvince = ''
            }
            if(this.store('address').selectStreet) {
                this.store('address').selectStreet = ''
            }
            if(this.store('shopping').serviceTime) {
                this.store('shopping').serviceTime = ''
            }
            if(this.store('address').addressContent) {
                this.store('address').addressContent = ''
            }
        },
        /**
         * 返回的时候 清除服务时间
         */
        clearServiceTime() {
            if(this.store('shopping').serviceTime) {
                this.store('shopping').serviceTime = ''
            }
            this.goPage('suggestion','',true)
        },
        /**
         * 提交订单唯一指定方法 检查数据
         */
        checkData() {

            if (!this.dealerCode) {
                this.showToast('请输入经销商编码！');
                return;
            }
            if (!this.dealerName) {
                this.showToast('经销商名称不能为空！');
                return;
            }
            if (!this.netWorkCode) {
                this.showToast('网点编号不能为空！');
                return;
            }
            if (!this.netWorkName) {
                this.showToast('网点名称不能为空！！');
                return;
            }
            if (this.serviceRequest[0] === '请选择') {
                this.showToast('请选择服务请求！');
                return;
            }
            if (this.serviceRequest[0] === '维修' && this.fault[0] === '请选择故障类型') {
                this.showToast('请选择故障类型！');
                return;
            }
            if (!this.userMobile) {
                this.showToast('请输入用户电话！');
                return;
            }
            if (!(/^1[3|4|5|7|8][0-9]\d{8}$/.test(this.userMobile))) {
                this.showToast('请输入正确的电话号码格式');
                return;
            }
            if (!this.userName) {
                this.showToast('请输入用户名称！');
                return;
            }
            if (!this.customerCompany) {
                this.showToast('请输入客户公司！');
                return;
            }

            // 根据街道字段判断有没有地址
            if (!this.addressItem.street) {
                this.showToast('请选择所在区域！');
                return;
            }
            if (!this.address) {
                this.showToast('请输入详细地址！');
                return;
            }
            if (!this.serviceTime.time) {
                this.showToast('请选择服务时间！');
                return;
            }

            //需要验证手机号是否有填，否则用户可以直接不填手机号，只输入个假的验证码通过验证
            if (this.isFirstBuy && !this.userPhone) {
                this.showToast('亲，请输入手机号！');
                return;
            }

            // 如果首次购买，则需要提示，输入验证码
            if (this.isFirstBuy && !this.imsCode) {
                // 如果是首次购买，则要输入验证码
                this.showToast('亲，请输入验证码！');
                return;
            }

            if (this.loadingQuery) {
                this.showToast('正在获取经销商信息,请稍候重试');
                return;
            }
            // 正在提交 直接返回
            if (this.hasCommit) {
                return;
            } else {
                this.hasCommit = true;
            }
            this.commitOrder();

        },
        /**
         * 用户第一次注册用户之后再提交
         **/
        register() {
            /**
             * 只能把参数当做Query String查询
             * 当做params请求会返回 openUserId、phone、msgContent不能为空
             */
            const params = {
                response_module_id: 3,
                interface_id: 67,
                phone: this.userPhone,
                msgContent: this.imsCode,
                openUserId: this.openIdBase64,
                appKey: this.appKey
            };

            this.api('suggestions').getRegister(params).then((succResp)=> {
                //  请求成功
                if (succResp.status) {
                    var data = succResp || {};
                    if (data.hasOwnProperty('content') && data.status && !data.error) {
                        this.api('common').bindPhone = true;
                        //TODO  暂不处理
                        this.getMixUser().then(function(response) {
                            this.store('common').userInfo = response
                        });
                        this.commitOrder();
                    } else {
                        this.showAlert(succResp.errorMsg || $conf.msg.errMsg);
                    }
                } else {
                    this.showAlert(succResp.errorMsg || $conf.msg.errMsg);
                }
                this.closeLoading();
            }, () =>{
                // 请求失败
                this.closeLoading();
                this.showAlert($conf.msg.errMsg);
            });

        },
        /**
         * @name commitOrder
         * @desc 提交订单
         **/
        commitOrder() {
            const userInfo = this.store('common').userInfo ? this.store('common').userInfo : {};
            let engineer;
            const tempEngineer = this.engineer[0] !== '请选择' || this.engineerPc !== '请选择';
            if(tempEngineer) {
                engineer = this.engineerInfoList[this.engineer[0]];
            }
            console.log(this.fault[0]);
            console.log(this.serviceRequest[0]);
            // 提交参数
            const params = {
                orderChannel: 4, // 订单渠道 1-美美家园服务号 2-网点推广 3-洗悦家服务号
                // 4-美居APP 5-工程师MMP 6-美的服务号 7-美的会员
                tradeFrom: '3', // 订单来源 1 美居APP; 2洗悦家服务号; 3美美家园服务号;
                brand: this.brand,
                appKey: this.appKey,
                uid: userInfo.uid,
                buyerNick: userInfo.nickName || userInfo.mobile || this.userPhone || this.addressItem.receiverName, // 用户昵称,如没有则填用户手机号
                openId: this.openId, // 用户在公众号下的唯一身份标识
                subscribeDate: this.serviceTime.date, // 预约上门日期	2015-11-26
                subscribeTime: this.serviceTime.time, // 1、08:00-12:00 2、12:00-16:00 3、16:00-20:00
                agentUnitCode: this.dealerCode, // 经销商编码
                agentUnitName: this.dealerName, // 经销商名称
                orderSource: {
                    "networkCode": this.netWorkCode, // 网点编码
                    "engineerPhone": tempEngineer ? engineer['engineerTel'] : '',
                    "engineerCode": tempEngineer ? engineer['engineerCode'] : '',
                    "engineerName": tempEngineer ? engineer['engineerName'] : '' // 工程师名称
                },
                orderItem: [ // 订单商品商品明细
                    {
                        goodsId: 1,
                        faultTypeId: '', // 故障类型	6
                        faultTypeCode: function (self) {
                            switch (self.serviceRequest[0]) {
                                case "维修":
                                    return self.faultMap[self.fault[0]].faultTypeCode;
                                    break;
                                case "用户要求退机":
                                    return "TH03001";
                                    break;
                                case "用户要求换机":
                                    return "TH03002";
                                    break;
                                case "安装-自动开机":
                                case "安装-手动开机":
                                    return "BZ01001";
                                    break;
                                default:
                                    return "";
                            }
                        }(this), // 故障类型编码(唯一标记)
                        faultTypeName: function (self) {
                            return self.isRepair ? self.faultMap[self.fault[0]].faultTypeName : self.serviceRequest[0];
                        }(this), // 故障类型名称
                        stoppageType: '', // 故障描述	压缩机不能正常启动，不制冷
                        itemCnt: parseInt(this.productNumber)
                    }
                ],
                startupMode: function (self) { // 自动开机 手动开机
                    switch (self.serviceRequest[0]) {
                        case "安装-自动开机":
                            return '10';
                        case "安装-手动开机":
                            return '11';
                        default:
                            return '';
                    }
                }(this),
                receiverPhone: userInfo.mobile || this.userPhone || '', //个人信息对应的手机号
                receiverMobile: this.userMobile || '', // 表单里面填的电话号码
                receiverName: this.userName || this.userMobile, // 地址里面的联系人名称
                customerCompany: this.customerCompany || '', // 客户公司
                goodsCode: '1123',
                goodsBrands: '美的', // 品牌
                goodsBrandId: 'MIDEA',
                goodsName: '租赁净水', // 产品名称
                goodsTypeId: 1, //产品类型Id 写死1
                sellerMemo: this.memo, // 卖家留言
                address: {
                    province: this.addressItem.province,
                    provinceName: this.addressItem.provinceName,
                    city: this.addressItem.city,
                    cityName: this.addressItem.cityName,
                    county: this.addressItem.county,
                    countyName: this.addressItem.countyName,
                    street: this.addressItem.street,
                    streetName: this.addressItem.streetName,
                    addr: this.address
                },
                accessMobile: this.userPhone,
                accessCode: this.imsCode
            };

            this.showLoading();
            this.api('appointment').addAppointmentAction(params).then(succResp => {

                if (succResp.code == 0 && succResp.msg =="操作成功") {
                    this.jumpAlertTxt = '亲，服务已经成功接受，我们将尽快分配附近的网点为您服务！';
                    this.jumpAlertShow = true;
                    this.hasCommit = false;
                    this.store('suggestions').setBindPhone = true;
//                    if (this.isFirstBuy) {
//                        this.getSelfUserInfo();
//                    }

                    // 统计
                    if (window.MtaH5) {
                        MtaH5.clickStat('baozhuangbaoxiu', {
                            'finish': 'true'
                        });
                    }
                } else {
                    this.showAlert(succResp.code + '错误信息：04025' + succResp.msg);

                }
                this.closeLoading();
            }, (res) => {
                // 请求失败
                this.hasCommit = false;

                this.closeLoading();
                this.showAlert($conf.msg.errMsg + '错误信息：04025' + res.status);

            });
        },
        /**
         * 发送验证码验证手机号
         */
        sendCode() {

            if (!this.userPhone) {
                this.showToast('亲，请输入您的手机号码！');
                return;
            }

            if (!/\d{11}/.test(this.userPhone)) {
                this.showToast('亲，手机号码格式错误！');
                return;
            }

            this.imsTxt = '剩余(' + this.timeLeave + 's)重发';
            this.timeOut = setInterval(function() {
                this.imsTxt = '剩余(' + this.timeLeave + 's)重发';
                this.timeLeave--;

                if (this.timeLeave === 0) {
                    clearInterval(this.timeOut);
                    this.imsTxt = '发送验证码';
                    this.timeLeave = 60; //重置计数，以防止第二次计数时从0开始
                }
            }, 1000);

            this.showLoading();

            /**
             * 发送验证码
             */
            let params = {
                phone: this.userPhone, // 手机号码
                openUserId: this.openIdBase64, // openId64位的
                source: 'midea' // 获取验证码接口专用
            };
            this.api('suggestions').getSMSCode(params).then((succResp)=> {
                // 请求成功
                if (succResp.status === true) {
                    let data = succResp || {};
                    if (data.hasOwnProperty('content') && data.status && !data.error) {
                        // 发送短信成功
                        this.showToast('亲，验证码已发送，请注意查收！');
                    } else {
                        this.showAlert(data.errMsg || $conf.msg.errMsg);
                    }
                } else {
                    this.showAlert(succResp.error.errMsg || $conf.msg.errMsg);
                }
                this.closeLoading();
            },(res)=> {
                // 请求失败
                this.closeLoading();
                this.showAlert(res);
            });
        }
    }
}

</script>
