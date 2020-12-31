/**
 * 正規表現用の定数クラス
 */
export namespace RegConst {
  /**
   * 半角英数の正規表現
   */
  export const HANKAKU_EISU = /^[0-9a-zA-Z]*$/
  /**
   * 全角ひらがなの正規表現
   */
  export const ZENKAKU_HIRAKANA = /^[ぁ-んー]*$/
  /**
   * 全角カナの正規表現
   */
  export const ZENKAKU_KANA = /^[ァ-ンヴー]*$/
  /**
   * 半角英数記号のみ
   */
  export const HANKAKU_EISU_KIGOU = /^[a-zA-Z0-9!-/:-@¥[-`{-~]*$/
  /**
   * emailアドレスの正規表現
   */
  export const EMAIL = /^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/
}