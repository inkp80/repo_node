module.exports = function(sequelize, DataTypes) {
  var courses = sequelize.define('lecture', {
	  id : { type : DataTypes.BIGINT(11).UNSIGNED, primaryKey: true, autoIncrement: true}
	  , lecture_id : { type : DataTypes.STRING(255) }
    , lecture_title : { type : DataTypes.STRING(255) }
    , grade : { type : DataTypes.STRING(255) }
    , credit : { type : DataTypes.INTEGER }
    , class_type : { type : DataTypes.STRING(255) }
    , place : { type : DataTypes.STRING(255) }
    , instructor : { type : DataTypes.STRING(255) }
    , eval_method : { type : DataTypes.STRING(255) }
    , remarks : { type : DataTypes.STRING(255) }
    , lecture_time : { type : DataTypes.STRING(255) }

    , url : { type : DataTypes.STRING(255) }
    , code : { type : DataTypes.STRING(255) }
    , active : { type : DataTypes.BOOLEAN }
    , term_id : { type : DataTypes.STRING(255) }
    , created_at: {
       type: 'TIMESTAMP',
       defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
       allowNull: false
     }
    , updated_at: {
       type: 'TIMESTAMP',
       defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
       allowNull: false}
  }
	,{
    timestamps: false,
	  tableName: 'lecture'
  });
  return courses;
};
