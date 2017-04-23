module.exports = function(sequelize, DataTypes) {
  var evaluation = sequelize.define('evaluation', {
	  id : { type : DataTypes.BIGINT(11).UNSIGNED, primaryKey: true, autoIncrement: true}
    , lecture_code : { type : DataTypes.STRING(255), unique: true }
    , lecture_title : { type : DataTypes.STRING(255) }
    , instructor : { type : DataTypes.STRING(255) }
    , eval_method : { type : DataTypes.STRING(255) }
    , class_type : { type : DataTypes.STRING(255) }
    , grade : { type : DataTypes.STRING(255) }
    , credit : { type : DataTypes.STRING(255) }
    , major : { type : DataTypes.STRING(255) }
    , predict_rating : { type : DataTypes.DOUBLE }
    , rating : { type : DataTypes.DOUBLE }
    , mae : { type : DataTypes.DOUBLE }
    , distinct_id : { type : DataTypes.STRING(255), unique: true }
    , url : { type : DataTypes.STRING(255) }
    , active : { type : DataTypes.BOOLEAN }
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
	  tableName: 'evaluation'
  });
  return evaluation;
};
