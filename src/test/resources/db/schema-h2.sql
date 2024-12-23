DROP TABLE IF EXISTS VCC_CARD;
create table VCC_CARD
(
    ID                        int   NOT NULL AUTO_INCREMENT PRIMARY KEY               ,
    VCC_TYPE                  int                  ,
    AMADEUS_NUM               varchar(128)         ,
    EXTERNAL                  varchar(128)         ,
    PRIMARY_ACCOUNT_NUM       varchar(64)          ,
    CARD_TYPE                 varchar(16)          ,
    PROVIDER                  varchar(128)         ,
    CARD_END_DATE             varchar(64)          ,
    CVV                       varchar(64)          ,
    AMOUNT                    decimal              ,
    CURRENCY                  varchar(8)           ,
    ON_CARD_AMOUNT            decimal              ,
    MAX_ALLOWED_TRANSACTION   int                  ,
    START_DATE                date                 ,
    END_DATE                  date                 ,
    PNR                       varchar(255)         ,
    ORDER_ITEM_NUM            long                  ,
    CARD_STATUS               int                  ,
    SYSTEM_TYPE               varchar(8)           ,
    CREATE_TIME               datetime             ,
    CREATED_BY                int                  ,
    LAST_UPDATE_TIME          datetime             ,
    LAST_UPDATED_BY           int                  ,
    ENABLED_FLAG              int                  ,
    PCC                       varchar(255)         ,
    CID                       int                  ,
    affiliate_confirmation_id varchar(255)         ,
    gateway_id                int
);



