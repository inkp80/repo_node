module.exports = function(sequelize, DataTypes) {
  var book = sequelize.define('book', {
	  id : { type : DataTypes.INTEGER.UNSIGNED, primaryKey: true, autoIncrement: true}
	  , name : { type : DataTypes.STRING(255) }
	  , loginTime : { type : DataTypes.DATE, defaultValue: '2002-06-05 00:00:00'
		  , get:function(){var convertTime=new Date(this.getDataValue('loginTime')); return convertTime.getTime()/1000;}}
  }, {
	  timestamps: false,
	  tableName: 'book'
  });
  return book;
};
