// pages/chesi/chesi.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name:'我是豆豆',
    age:1000

  },
  dianji:function(){
    console.log('一直点我')
  },
  changanwo:function(){
    console.log('一直长安我')
  },
  test:function(){
    wx.request({
      url: 'http://127.0.0.1:8000/api/v1.0/image/',
      method:'GET',
      header:{},
      success:function(res){
        console.log('结果success:'+res.data)
      },
      fail:function(res){
        console.log('结果fail:'+res.errMsg)
      }
    })
  },
  save:function(){
    console.log('保存成功')
    wx.setStorage({
      key: 'text',
      data: '我是保存的数据',
    })
  },
  read:function(){
    console.log('读取失败')
    wx.getStorage({
      key: 'text',
      success: function(res) {
        console.log('读取成功'+res.data)
      },
    })
  },
  remove:function(res){
    wx.removeStorage({
      key: 'text',
      success: function(res) {
        console.log('remove ok')
        //console.log('remove'+key+'成功!!')
      },
    })
  },
  clear:function(){
    console.log('clear me lll')
    wx.clearStorage()
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})