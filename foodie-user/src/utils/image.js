/**
 * 图片URL处理工具
 */

// 后端服务器地址
const BASE_URL = 'http://localhost:8080'

/**
 * 获取完整的图片URL
 * @param {string} imagePath - 数据库中的图片路径，如 '/upload/xxx.jpg'
 * @returns {string} 完整的图片URL
 */
export function getImageUrl(imagePath) {
  if (!imagePath) return ''
  
  // 如果已经是完整URL，直接返回
  if (imagePath.startsWith('http')) {
    return imagePath
  }
  
  // 如果是相对路径，拼接后端地址
  if (imagePath.startsWith('/upload/')) {
    return BASE_URL + imagePath
  }
  
  // 如果路径不是以/upload/开头，添加前缀
  return BASE_URL + '/upload/' + imagePath
}

/**
 * 处理多个图片路径（逗号分隔）
 * @param {string} imagePathsStr - 逗号分隔的图片路径字符串
 * @returns {string[]} 完整的图片URL数组
 */
export function getImageUrls(imagePathsStr) {
  if (!imagePathsStr) return []
  
  return imagePathsStr.split(',')
    .map(path => path.trim())
    .filter(path => path)
    .map(path => getImageUrl(path))
}